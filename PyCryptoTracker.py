# Dependencies:
# python -m pip install requests

import requests

url = "https://api.coingecko.com/api/v3/ping"

# For professional subscriptions, switch "x-cg-pro-api-key" with "x-cg-demo-api-key"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "apikey"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")



class py