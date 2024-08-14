from scholarly import scholarly
from scholarly import ProxyGenerator
import json
import os

def fetch_google_scholar_citations():
    # Set up a ProxyGenerator using Selenium
    pg = ProxyGenerator()
    success = pg.SeleniumWebDriver()
    scholarly.use_proxy(pg)

    # Search for the author
    search_query = scholarly.search_author('Efstathios Magerakis')
    try:
        author = next(search_query)
    except StopIteration:
        print("Author not found.")
        return

    author_filled = scholarly.fill(author)

    # Fetch citation metrics
    citations = author_filled.get('citedby', 'N/A')
    h_index = author_filled.get('hindex', 'N/A')
    i10_index = author_filled.get('i10index', 'N/A')

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
