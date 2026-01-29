from serpapi import GoogleSearch
import json
import os
import sys
from datetime import datetime

def fetch_google_scholar_citations():
    api_key = os.environ.get("SERPAPI_KEY")
    if not api_key:
        print("Error: SERPAPI_KEY environment variable is not set.")
        sys.exit(1)

    params = {
        "engine": "google_scholar_author",
        "author_id": "LxLY15EAAAAJ&hl",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Access the cited_by dictionary to get the citation metrics
    if "cited_by" in results:
        citations = results["cited_by"]["table"][0]["citations"]["all"]
        h_index = results["cited_by"]["table"][1]["h_index"]["all"]
        i10_index = results["cited_by"]["table"][2]["i10_index"]["all"]
    else:
        print("'cited_by' information not found in the response.")
        sys.exit(1)

    # Prepare the metrics for display
    metrics = {
        'total_citations': citations,
        'h_index': h_index,
        'i10_index': i10_index,
        'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Save the metrics to a JSON file
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/google_scholar_citations.json', 'w') as f:
        json.dump(metrics, f, indent=2)

    # Generate styled HTML content for English and Greek versions
    styled_html_content = f"""<div style="background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; max-width: 400px; margin: 20px auto; font-family: Arial, sans-serif;">
    <h4 style="color: #4285F4; text-align: center; margin: 0 0 10px 0; font-size: 18px; font-weight: normal;">Google Scholar Metrics</h4>
    <div style="display: flex; justify-content: space-between; text-align: center;">
        <div>
            <p style="font-size: 24px; font-weight: bold; margin: 0; color: #333;">{citations}</p>
            <p style="margin: 0; color: #666; font-size: 12px;">Citations</p>
        </div>
        <div>
            <p style="font-size: 24px; font-weight: bold; margin: 0; color: #333;">{h_index}</p>
            <p style="margin: 0; color: #666; font-size: 12px;">H-Index</p>
        </div>
        <div>
            <p style="font-size: 24px; font-weight: bold; margin: 0; color: #333;">{i10_index}</p>
            <p style="margin: 0; color: #666; font-size: 12px;">i10-Index</p>
        </div>
    </div>
</div>
"""

    # Generate simple HTML content for partials
    simple_html_content = f"""
    <div class="google-scholar-metrics">
        <h3>Google Scholar Metrics</h3>
        <p>Citations: {citations}</p>
        <p>H-Index: {h_index}</p>
        <p>i10-Index: {i10_index}</p>
    </div>
    """

    # Update all HTML files
    files_to_update = [
        ('content/english/google_scholar_metrics.html', styled_html_content),
        ('content/greek/google_scholar_metrics.html', styled_html_content),
        ('layouts/partials/google_scholar_metrics.html', simple_html_content)
    ]

    for file_path, content in files_to_update:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated: {file_path}")

    print(f"\nGoogle Scholar Metrics Updated:")
    print(f"Citations: {citations}")
    print(f"H-Index: {h_index}")
    print(f"i10-Index: {i10_index}")
    print(f"Last Updated: {metrics['last_updated']}")

if __name__ == "__main__":
    fetch_google_scholar_citations()
