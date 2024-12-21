import requests
import json

def create_splunk_search_job(base_url, username, password, search_query, output_mode="json"):
    search_endpoint = f"{base_url}/services/search/jobs"

    # Define the payload for the search job
    data = {
        'search': search_query,
        'output_mode': output_mode,
        'exec_mode': 'oneshot'
    }

    # Perform the POST request with basic authentication
    response = requests.post(
        search_endpoint,
        data=data,
        auth=(username, password),  # Basic authentication
        verify=False  # Set to True if using valid SSL certificates
    )

    return response.json()

# Example usage
base_url = "https://localhost:8089"  # Splunk management port
username = "admin"
password = "yourpassword"  # Replace with your password
search_query = "search index=_internal | head 10"

result = create_splunk_search_job(base_url, username, password, search_query)
for item in result.get('results'):
    print(item)
