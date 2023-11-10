import requests

postman_api_key = "YOUR_POSTMAN_API_KEY"
collection_id = "YOUR_COLLECTION_ID"

# Create a new collection
response = requests.post(
    f"https://api.getpostman.com/collections",
    headers={"X-Api-Key": postman_api_key},
    json={"name": "My Collection"}
)
new_collection = response.json()

# Import the API into the collection
import_url = "URL_TO_MULESOFT_API_SPEC"
response = requests.post(
    f"https://api.getpostman.com/collections/{new_collection['uid']}/import",
    headers={"X-Api-Key": postman_api_key},
    json={"type": "link", "link": import_url}
)

if response.status_code == 200:
    print("API imported successfully.")
else:
    print("API import failed.")
