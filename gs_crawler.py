from serpapi import GoogleSearch
import json
import os

def fetch_google_scholar_citations():
    params = {
        "engine": "google_scholar_author",
        "author_id": "LxLY15EAAAAJ&hl",  # Replace with your actual author ID
        "api_key": "69ae21c80d3652e44395934f0ef271cc26e6a13a8d287a01f55fc4ae02b8da23"   # Replace with your SerpApi key
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
        return

    # Prepare the metrics for display
    metrics = {
        'total_citations': citations,
        'h_index': h_index,
        'i10_index': i10_index
    }

    # Save the metrics to a JSON file
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/google_scholar_citations.json', 'w') as f:
        json.dump(metrics, f)

    # Generate HTML snippet
    if not os.path.exists('static'):
        os.makedirs('static')
    html_content = f"""
    <div class="google-scholar-metrics">
        <h3>Google Scholar Metrics</h3>
        <p>Citations: {citations}</p>
        <p>H-Index: {h_index}</p>
        <p>i10-Index: {i10_index}</p>
    </div>
    """

    # Save the HTML snippet to a file
    with open('static/google_scholar_metrics.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    fetch_google_scholar_citations()
