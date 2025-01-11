# Dependencies:
# python -m pip install requests

'''
To-do:
1. crypto_data: current price, price exchange 24h, Historical prices if supported by API, Currency to view exchange rates in
2. market_data: Market Capitalization, Total Volume (24h), Circulating Supply, Max Supply
4. exchange_rates: Allows you to query BTC exchange rates with other currencies.
5. search_queries: Allows you to search for coins, categories and markets listed on CoinGecko.
'''


import requests

class PyCT:
    """
    @class PyCT
    @brief A class to interact with the CoinGecko API to fetch cryptocurrency data.

    This class provides methods for retrieving cryptocurrency data from the CoinGecko API. 
    The primary function is to fetch data for specified cryptocurrencies, which can be customized 
    with various parameters and endpoints.

    @note For professional API subscriptions, replace the "x-cg-pro-api-key" header with "x-cg-demo-api-key". 
          The endpoint "https://api.coingecko.com/api/v3/ping" should also be updated to 
          "https://pro_api.coingecko.com/api/v3/ping" for pro users.

    @see https://www.coingecko.com for CoinGecko API documentation.
    """

    
    def __init__(self, api_key):
            self._url = "https://api.coingecko.com/api/v3/ping"     # Endpoint for market data (DEMO URL)
            self._api_key = api_key                                 # Store the API key
            self._headers = {
                "accept": "application/json",
                "x-cg-demo-api-key": self._api_key
            }

    def get_crypto_data(self, coins, currency="usd", include_market_data=False):
        


        # Prepare query parameters dynamically based on the function inputs
        params = {
            "ids": ",".join(coins),          # List of coins as a comma-separated string
            "vs_currency": currency,         # Currency to compare (e.g., 'usd')
            "order": "market_cap_desc",      # Sort by market cap
            "per_page": len(coins),          # Limit the number of results to the number of requested coins
            "page": 1                        # First page of results
        }

        # Add extra parameters if market data is requested
        if include_market_data:
            params["sparkline"] = "false"  # Example: Exclude sparkline data for simplicity

        # Send the GET request with parameters
        response = requests.get(self._url, headers=self._headers, params=params)

        # Check the response status
        if response.status_code == 200:
            return response.json()  # Return the data as a Python list of dictionaries
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None



# Example usage:
def test_function():
    # Initialize the class with your API key
    api_key = "CG-aTnmuupTErMjud8p9vbPqVYS"
    crypto_fetcher = PyCT(api_key)

    # Call the method to get data for multiple coins
    coins = ["bitcoin", "ethereum", "cardano"]
    data = crypto_fetcher.TC_get_crypto_data(coins, currency="usd", include_market_data=True)

    # Print the data for each coin
    if data:
        for coin_data in data:
            print(f"{coin_data['name']} ({coin_data['symbol'].upper()}):")
            print(f"  Price: ${coin_data['current_price']}")
            print(f"  Market Cap: ${coin_data['market_cap']}")
            print(f"  24h Volume: ${coin_data['total_volume']}\n")



# Run this file directly to test the api key and CoinGecko server status without the class: {'gecko_says': '(V3) To the Moon!'}
if __name__ == "__main__":
    url = "https://api.coingecko.com/api/v3/ping"

    # For professional subscriptions, switch "x-cg-pro-api-key" with "x-cg-demo-api-key"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-aTnmuupTErMjud8p9vbPqVYS"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")


    test_function()



    

