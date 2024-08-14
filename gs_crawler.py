import scholarly
import json
import os

def fetch_google_scholar_citations():
    # Replace 'Your Name' with your actual name as it appears on Google Scholar
    search_query = scholarly.search_author('Efstathios Magerakis')
    author = next(search_query)
    
    citations = {
        'total_citations': author.citedby,
        'h_index': author.hindex,
        'i10_index': author.i10index
    }
    
    # Save the citation data to a JSON file
    with open('data/google_scholar_citations.json', 'w') as f:
        json.dump(citations, f)

if __name__ == "__main__":
    fetch_google_scholar_citations()
