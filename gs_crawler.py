from serpapi import GoogleSearch
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime

GS_AUTHOR_ID = "LxLY15EAAAAJ"
ORCID = "0000-0001-7977-0363"
SCOPUS_JSON = "data/scopus_citations.json"


def write_json(name, data):
    # data/ is read by Hugo; static/data/ is served over HTTP
    for folder in ("data", "static/data"):
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, name), "w") as f:
            json.dump(data, f, indent=2)


def fetch_google_scholar():
    api_key = os.environ.get("SERPAPI_KEY")
    if not api_key:
        print("Error: SERPAPI_KEY environment variable is not set.")
        sys.exit(1)

    params = {
        "engine": "google_scholar_author",
        "author_id": GS_AUTHOR_ID,
        "hl": "en",
        "api_key": api_key
    }
    results = GoogleSearch(params).get_dict()

    # Access the cited_by dictionary to get the citation metrics
    if "cited_by" not in results:
        print("'cited_by' information not found in the response.")
        sys.exit(1)

    table = results["cited_by"]["table"]
    return {
        'total_citations': table[0]["citations"]["all"],
        'h_index': table[1]["h_index"]["all"],
        'i10_index': table[2]["i10_index"]["all"],
        'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def load_previous_scopus():
    try:
        with open(SCOPUS_JSON) as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def fetch_scopus():
    """Return Scopus metrics, or the last saved ones if the API can't be used.

    Scopus is optional: a missing key or API error must not stop the
    Google Scholar update.
    """
    api_key = os.environ.get("SCOPUS_API_KEY")
    if not api_key:
        print("SCOPUS_API_KEY not set; skipping Scopus.")
        return load_previous_scopus()

    # Look the author up by Scopus ID if given, otherwise by ORCID
    author_id = os.environ.get("SCOPUS_AUTHOR_ID")
    if author_id:
        url = f"https://api.elsevier.com/content/author/author_id/{author_id}?view=METRICS"
    else:
        url = f"https://api.elsevier.com/content/author/orcid/{ORCID}?view=METRICS"

    request = urllib.request.Request(url, headers={
        "X-ELS-APIKey": api_key,
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            results = json.load(response)
        author = results["author-retrieval-response"][0]
        core = author["coredata"]
        scopus_id = core["dc:identifier"].split(":")[-1]
        metrics = {
            'total_citations': int(core.get("citation-count") or core["cited-by-count"]),
            'h_index': int(author["h-index"]),
            'documents': int(core["document-count"]),
            'author_id': scopus_id,
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except (urllib.error.URLError, KeyError, IndexError, ValueError, TypeError) as e:
        print(f"Warning: could not fetch Scopus metrics ({e}); keeping previous values.")
        return load_previous_scopus()

    write_json("scopus_citations.json", metrics)
    return metrics


def stat(value, label):
    return f"""            <div>
                <p style="font-size: 24px; font-weight: bold; margin: 0; color: #333;">{value}</p>
                <p style="margin: 0; color: #666; font-size: 12px;">{label}</p>
            </div>
"""


def section(title, color, link, stats):
    return f"""    <h4 style="text-align: center; margin: 0 0 10px 0; font-size: 18px; font-weight: normal;"><a href="{link}" target="_blank" rel="noopener" style="color: {color}; text-decoration: none;">{title}</a></h4>
    <div style="display: flex; justify-content: space-between; text-align: center;">
{"".join(stat(v, l) for v, l in stats)}    </div>
"""


def render_box(gs, scopus):
    parts = [section(
        "Google Scholar Metrics", "#4285F4",
        f"https://scholar.google.com/citations?user={GS_AUTHOR_ID}&hl=en",
        [(gs['total_citations'], "Citations"), (gs['h_index'], "H-Index"), (gs['i10_index'], "i10-Index")])]
    if scopus:
        parts.append(section(
            "Scopus Metrics", "#E9711C",
            f"https://www.scopus.com/authid/detail.uri?authorId={scopus['author_id']}",
            [(scopus['total_citations'], "Citations"), (scopus['h_index'], "H-Index"), (scopus['documents'], "Documents")]))
    divider = '    <hr style="border: 0; border-top: 1px solid #e0e0e0; margin: 15px 0;">\n'
    return ('<div style="background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; max-width: 400px; margin: 20px auto; font-family: Arial, sans-serif;">\n'
            + divider.join(parts) + "</div>\n")


def render_simple(gs, scopus):
    html = f"""
    <div class="google-scholar-metrics">
        <h3>Google Scholar Metrics</h3>
        <p>Citations: {gs['total_citations']}</p>
        <p>H-Index: {gs['h_index']}</p>
        <p>i10-Index: {gs['i10_index']}</p>
    </div>
    """
    if scopus:
        html += f"""<div class="scopus-metrics">
        <h3>Scopus Metrics</h3>
        <p>Citations: {scopus['total_citations']}</p>
        <p>H-Index: {scopus['h_index']}</p>
        <p>Documents: {scopus['documents']}</p>
    </div>
    """
    return html


def main():
    gs = fetch_google_scholar()
    write_json("google_scholar_citations.json", gs)
    scopus = fetch_scopus()

    box = render_box(gs, scopus)
    files_to_update = [
        ('content/english/google_scholar_metrics.html', box),
        ('content/greek/google_scholar_metrics.html', box),
        ('layouts/partials/google_scholar_metrics.html', render_simple(gs, scopus))
    ]
    for file_path, content in files_to_update:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated: {file_path}")

    print(f"\nGoogle Scholar: {gs['total_citations']} citations, h-index {gs['h_index']}, i10-index {gs['i10_index']}")
    if scopus:
        print(f"Scopus: {scopus['total_citations']} citations, h-index {scopus['h_index']}, {scopus['documents']} documents")


if __name__ == "__main__":
    main()
