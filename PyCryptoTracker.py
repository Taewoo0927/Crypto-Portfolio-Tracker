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

    def precise_data_extraction(self, object, labels, keys, json_data):
        # Extract specific data from PRECISE searching. 
        # Case Sensitive. 
        # Function will pick the object on the first page, top of the list.


        # Check if the response is a dictionary
        if isinstance(json_data, dict):
            data = json_data.get(object, [])
            if data:
                # If data exists and is a list of dictionaries
                if isinstance(data, list) and isinstance(data[0], dict):
                    data = data[0]  # Grab the first dictionary
                    extract = [data.get(key) for key in keys]  # Extract the desired values
                    sendData = dict(zip(labels, extract))
                    return sendData
                else:
                    print(f"Error: Unexpected format inside the list for object {object}. Expected a list of dictionaries.")
                    print(json_data)
                    return None
            else:
                print(f"Error: No data found for {object}")
                print(json_data)
                return None

        # Check if the response is a list
        elif isinstance(json_data, list):

            # Handle list of dictionaries
            if isinstance(json_data[0], dict):
                data = json_data[0]  # Grab the first dictionary
                extract = [data.get(key) for key in keys]  # Extract the desired values
                sendData = dict(zip(labels, extract))
                return sendData
            
            # Handle list of lists
            elif isinstance(json_data[0], list):
                if len(json_data) == len(labels):
                    sendData = dict(zip(labels, json_data))
                    return sendData
                else:
                    print(f"Error: The number of elements in the list does not match the number of labels.")
                    return None
            else:
                print("Error: Unexpected data format inside the list.")
                return None

        else:
            print("Error: Unexpected data format. Neither a list nor a dictionary.")
            return None




    # Search
    def search_coin(self, coin_name):
        url = "https://api.coingecko.com/api/v3/search"
        headers = {"accept": "application/json"}
        params = {"query": coin_name}  # Required!

        # Get data from the API
        response = requests.get(url, headers=headers, params=params)
        json_data = response.json()

        # Define labels, keys, and object
        labels = ["coin_iD", "coin_name", "api_symbol", "symbol", "market_cap_rank", "thumb", "large"]
        keys = ["id", "name", "api_symbol", "symbol", "market_cap_rank", "thumb", "large"]
        objectParam = "coins"

        # Use the data_extraction function to extract and format the data
        return self.precise_data_extraction(objectParam, labels, keys, json_data)

        


    # Coins
    def coins_retrieve_id(self, coin_name):
        # Retrieves and prints data for a coin.
        url = "https://api.coingecko.com/api/v3/coins/list"
        headers = {"accept": "application/json"}
        params = {"include_platform": False}


        # Get data from the API
        response = requests.get(url, headers=headers,params=params)
        json_data = response.json()

        # Loop through all coins and find the one matching the coin_name
        for coin in json_data:
            if coin['name'].lower() == coin_name.lower():
                return {
                    'coin_id': coin['id'],
                    'coin_name': coin['name'],
                    'symbol': coin['symbol']
                }

    def coins_historical_market_data(self, coin_id, date="01-01-2025", localization=False):
        # Retrieves and prints historical data for a coin on a certain day in the format dd-mm-yyyy
        # get current_price, market_cap, total_volume at a specified date

        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history"
        headers = {"accept": "application/json"}
        params = {
            "date": date,
            "localization": localization
            }  # Include the date and localization parameters

        # Get data from the API
        response = requests.get(url, headers=headers, params=params)
        json_data = response.json()

        # Define labels and keys
        labels = ["current_price", "market_cap", "total_volume"]
        keys = ["current_price", "market_cap", "total_volume"]
        objectParam = "market_data"

        # Use the data_extraction function to extract and format the data
        return self.precise_data_extraction(objectParam, labels, keys, json_data)
    
    def coins_historical_chart_data(self, coin_id, vs_currency="usd", days=1, interval="daily", precision="1"):
        # Retrieves and prints historical chart data for a coin.
        # Days = previous days to retrieve data for.
        # interval = data interval (daily, weekly?, yearly?).
        # precision is the number of decimal places to return in the response.

        url = f" https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        headers = {"accept": "application/json"}
        params = {
            "vs_currency": vs_currency, 
            "days": days,
            "interval": interval,
            "precision": precision
            }  # Include the date and localization parameters

        # Get data from the API
        response = requests.get(url, headers=headers, params=params)
        json_data = response.json()

        # Define labels and keys
        labels = ["prices", "market_caps", "total_volumes"]
        keys = ["prices", "market_caps", "total_volumes"]
        objectParam = None

        # Use the data_extraction function to extract and format the data
        return self.precise_data_extraction(objectParam, labels, keys, json_data)



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
    cryptoTracker = PyCT("CG-aTnmuupTErMjud8p9vbPqVYS")
    print(cryptoTracker.coins_historical_market_data("bitcoin"))

    
    



    

