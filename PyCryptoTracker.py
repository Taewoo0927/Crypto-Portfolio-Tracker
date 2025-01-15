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
    def __init__(self, api_key):
            self._url = "https://api.coingecko.com/api/v3/ping"     # Endpoint for market data (DEMO URL)
            self._api_key = api_key                                 # Store the API key
            self._headers = {
                "accept": "application/json",
                "x-cg-demo-api-key": self._api_key
            }


    def search_coin(self, coin_name):

        url = "https://api.coingecko.com/api/v3/search"
        headers = {"accept": "application/json"}
        params = {"query": coin_name} # Required!

        # Get data from the API
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # Extract specific data about the coin
        coins = data.get('coins', [])
        if coins:
            coin = coins[0]  # Get the first coin in the list

            # Get Data from Keys
            labels = ["Coin ID", "Coin Name","Api Symbol", "Symbol", "Market Cap Rank", "Thumb", "Large"]
            keys = ["id", "name", "api_symbol", "symbol", "market_cap_rank", "thumb", "large"]

            alists = [coin.get(key) for key in keys]

            # Format Data
            sendData = dict(zip(labels, alists))
        
            return sendData
        else:
            return response.status_code
        

    def search_exchanges(self, coin_name):

        url = "https://api.coingecko.com/api/v3/search"
        headers = {"accept": "application/json"}
        params = {"query": coin_name} # Required!

        # Get data from the API
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # Extract specific data about the coin
        coins = data.get('coins', [])
        if coins:
            coin = coins[0]  # Get the first coin in the list

            # Get Data from Keys
            labels = ["Coin ID", "Coin Name","Market Type", "Thumb", "Large"]
            keys = ["id", "name", "market_type", "thumb", "large"]

            alists = [coin.get(key) for key in keys]

            # Format Data
            sendData = dict(zip(labels, alists))
        
            return sendData
        else:
            return response.status_code
        


    def BTC_to_Currency_ExchRate(self, coin_name):

        url = "https://api.coingecko.com/api/v3/exchange_rates"
        headers = {"accept": "application/json"}

        # Get data from the API
        response = requests.get(url, headers=headers)
        data = response.json()

        # Extract specific data about the coin
        coins = data.get('coins', [])
        if coins:
            coin = coins[0]  # Get the first coin in the list

            # Get Data from Keys
            labels = ["Coin ID", "Coin Name","Market Type", "Thumb", "Large"]
            keys = ["id", "name", "market_type", "thumb", "large"]

            alists = [coin.get(key) for key in keys]

            # Format Data
            sendData = dict(zip(labels, alists))
        
            return sendData
        else:
            return response.status_code


    #def get_crypto_data(self, coins, currency="usd", include_market_data=False):
        
  



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


    # Testing Area
    testMarket = PyCT("CG-aTnmuupTErMjud8p9vbPqVYS")
    print(testMarket.search_coin("bitcoin"))

    



    

