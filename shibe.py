import requests

api_url = "http://shibe.online/api/shibes?count=1"

params = {
    "count": 10
}

response = requests.get(api_url, params=params)

print(f"Response status code is: {response.status_code}")

response_json = response.json()

print("Here is a list of URLs for dog pictures:")
for url in response_json:
    print(f"\t {url}")
