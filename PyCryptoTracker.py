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

    # Ping API
    def ping_API_server(self):

        url = "https://api.coingecko.com/api/v3/ping"

        response = requests.get(url, headers=self._headers)

        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}, {response.text}"

    # Data Getters
    def search_query(self, search_query, precise = True):
        # Returns first coin listed

        url = "https://api.coingecko.com/api/v3/search"
        params = {"query": search_query} # Required!

        # Get data from the API
        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        # Extract specific data about the coin
        coins = data.get('coins', [])

        if precise:
            coin = coins[0]  # Get the first coin in the list

        # Check if there is data to return
        if coin: 
            return coin
        else:
            return response.status_code
        
    def exchange_data(self, coin_id):

        url = f"https://api.coingecko.com/api/v3/exchanges/{coin_id}"

        # Get data from the API
        response = requests.get(url, headers=self._headers)
        data = response.json()

        # Check if there is data to return
        if data: 
            return data
        else:
            return response.status_code
        
    def coins_coin_data(self, coin_id, localization = False, tickers = False, market_data = False, community_data = False, developer_data = False, sparkline = False):

        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"

        params = {
            "localization": localization,
            "tickers": tickers, 
            "market_data": market_data,    
            "community_data": community_data,
            "developer_data": developer_data,
            "sparkline": sparkline  
            }
        
        # Get data from the API
        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()


        # Check if there is data to return
        if data: 
            return data
        else:
            return response.status_code

    def coins_coin_market_page(self, coin_id, precise = True, vs_currency = False, category = False, order = "market_cap_desc", per_page = 50, page = 1, sparkline = False, price_change_percentage = "1h", locale = False, precision = False):

        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"

        params = {
            "vs_currency": vs_currency,
            "category": category,
            "order": order,
            "per_page": per_page,
            "page": page,
            "sparkline": sparkline,
            "price_change_percentage": price_change_percentage,
            "locale": locale,
            "precision": precision
            }
        
        # Get data from the API
        response = requests.get(url, self._headers, params=params)
        data = response.json()

        if precise:
            market_data = data[0]  # Get the first coin in the list
        else:
            market_data = data

        # Check if there is data to return
        if market_data: 
            return market_data
        else:
            return response.status_code


    # CHARTS
    def coins_chart_historical_timerange(self, coin_id, vs_currency, from_date, to_date, decimal_precision="2"):
        # Pst 365 days only (demo plan)

        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
        params = {
            "vs_currency": vs_currency,
            "from": from_date,  # Unix timestamp
            "to": to_date,     # Unix timestamp
            "precision": decimal_precision    # Optional
            }

        # Get data from the API
        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        # Check if there is data to return
        if data: 
            return data
        else:
            return response.status_code
    
    def coins_chart_historical_interval(self, coin_id, vs_currency, num_days_ago, interval, decimal_precision="2"):
        # Past 365 days only (demo plan)

        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": vs_currency,
            "days": num_days_ago,  # Data up to number of days ago
            "interval": interval,     # data interval
            "precision": decimal_precision    # Optional
            }

        # Get data from the API
        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        # Check if there is data to return
        if data: 
            return data
        else:
            return response.status_code
        
    def exchanges_chart_volume(self, coin_id, num_days_ago):
        # Past 365 days only (demo plan)

        url = f"https://api.coingecko.com/api/v3/exchanges/{coin_id}/volume_chart"
        params = {
            "days": num_days_ago,  # Data up to number of days ago
            }

        # Get data from the API
        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        # Check if there is data to return
        if data: 
            return data
        else:
            return response.status_code
        
    def coins_chart_OHLC(self, coin_id, vs_currency, num_days_ago, decimal_precision="2"):
        # Past 365 days only (demo plan)

        url = f"https://api.coingecko.com/api/v3/exchanges/{coin_id}/volume_chart"
        params = {
            "vs_currency": vs_currency,
            "days": num_days_ago,  # Data up to number of days ago
            "precision": decimal_precision    # Optional
            }

        # Get data from the API
        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        # Check if there is data to return
        if data: 
            return data
        else:
            return response.status_code




# Run this file directly to test the api key and CoinGecko server status without the class: {'gecko_says': '(V3) To the Moon!'}
if __name__ == "__main__":

    # Testing Area
    testMarket = PyCT("CG-aTnmuupTErMjud8p9vbPqVYS")
    print(testMarket.ping_API_server())

    



    

