from opensearchpy import OpenSearch

def search_pdfs(client, index_name, query_text):
    """
    Search for keywords in the indexed PDFs.
    """
    query = {
        "query": {
            "match": {
                "text": query_text
            }
        },
        "highlight": {
            "fields": {
                "text": {}
            }
        }
    }
    
    try:
        response = client.search(index=index_name, body=query)
        hits = response["hits"]["hits"]
        print(f"Found {len(hits)} matching documents:")
        for hit in hits:
            print(f"\nFile: {hit['_source']['file_name']}")
            print(f"Score: {hit['_score']}")
            print("Highlights:")
            for highlight in hit.get("highlight", {}).get("text", []):
                print(f"  - {highlight}")
            print(f"Metadata: {hit['_source']['metadata']}")
    except Exception as e:
        print(f"Error during search: {str(e)}")

if __name__ == "__main__":
    # OpenSearch connection settings
    INDEX_NAME = "university-pdfs"
    HOST = "localhost"
    PORT = 9200
    AUTH = ("admin", "Respvblica.118")
    
    # Initialize OpenSearch client
    client = OpenSearch(
        hosts=[{"host": HOST, "port": PORT}],
        http_auth=AUTH,
        use_ssl=False,
        verify_certs=False,
        ssl_show_warn=False
    )
    
    # Perform a search
    QUERY_TEXT = input("Write down your query:\n")
    search_pdfs(client, INDEX_NAME, QUERY_TEXT)
