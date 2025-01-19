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
    '''
    @brief A class to interact with the CoinGecko API.
    '''
    def __init__(self, api_key):
        '''
        @brief Initializes the PyCT class with the provided API key.
        @param api_key The API key for authentication.
        '''
        self._url = "https://api.coingecko.com/api/v3/ping"     # Endpoint for market data (DEMO URL)
        self._api_key = api_key                                 # Store the API key
        self._headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": self._api_key
        }

    def ping_API_server(self):
        '''
        @brief Pings the CoinGecko API server to check its status.
        @return The server response in JSON format if successful, otherwise an error message.
        '''
        url = "https://api.coingecko.com/api/v3/ping"
        response = requests.get(url, headers=self._headers)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}, {response.text}"

    def search_query(self, search_query, precise=True):
        '''
        @brief Searches for coins, categories, and markets listed on CoinGecko.
        @param search_query The search query string.
        @param precise If True, returns the first coin listed.
        @return The first coin listed if precise is True, otherwise the full response.
        '''
        url = "https://api.coingecko.com/api/v3/search"
        params = {"query": search_query}

        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()
        coins = data.get('coins', [])

        if precise and coins:
            coin = coins[0]  # Get the first coin in the list

        if coin:
            return coin
        else:
            return response.status_code

    def exchange_data(self, coin_id):
        '''
        @brief Retrieves exchange data for a specific coin.
        @param coin_id The ID of the coin.
        @return The exchange data in JSON format if successful, otherwise the status code.
        '''
        url = f"https://api.coingecko.com/api/v3/exchanges/{coin_id}"
        response = requests.get(url, headers=self._headers)
        data = response.json()

        if data:
            return data
        else:
            return response.status_code

    def coins_coin_data(self, coin_id, localization=False, tickers=False, market_data=False, community_data=False, developer_data=False, sparkline=False):
        '''
        @brief Retrieves detailed data for a specific coin.
        @param coin_id The ID of the coin.
        @param localization If True, includes localization data.
        @param tickers If True, includes tickers data.
        @param market_data If True, includes market data.
        @param community_data If True, includes community data.
        @param developer_data If True, includes developer data.
        @param sparkline If True, includes sparkline data.
        @return The coin data in JSON format if successful, otherwise the status code.
        '''
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
        params = {
            "localization": localization,
            "tickers": tickers,
            "market_data": market_data,
            "community_data": community_data,
            "developer_data": developer_data,
            "sparkline": sparkline
        }

        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        if data:
            return data
        else:
            return response.status_code

    def coins_coin_market_page(self, coin_id, precise=True, vs_currency=False, category=False, order="market_cap_desc", per_page=50, page=1, sparkline=False, price_change_percentage="1h", locale=False, precision=False):
        '''
        @brief Retrieves market data for a specific coin.
        @param coin_id The ID of the coin.
        @param precise If True, returns the first coin listed.
        @param vs_currency The target currency for exchange rates.
        @param category The category of the coin.
        @param order The order of the results.
        @param per_page The number of results per page.
        @param page The page number.
        @param sparkline If True, includes sparkline data.
        @param price_change_percentage The time period for price change percentage.
        @param locale The locale for the data.
        @param precision The precision of the data.
        @return The market data in JSON format if successful, otherwise the status code.
        '''
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

        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        if precise:
            market_data = data[0]  # Get the first coin in the list
        else:
            market_data = data

        if market_data:
            return market_data
        else:
            return response.status_code

    def coins_chart_historical_timerange(self, coin_id, vs_currency, from_date, to_date, decimal_precision="2"):
        '''
        @brief Retrieves historical market data for a specific coin within a time range.
        @param coin_id The ID of the coin.
        @param vs_currency The target currency for exchange rates.
        @param from_date The start date (Unix timestamp).
        @param to_date The end date (Unix timestamp).
        @param decimal_precision The precision of the data.
        @return The historical market data in JSON format if successful, otherwise the status code.
        '''
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
        params = {
            "vs_currency": vs_currency,
            "from": from_date,
            "to": to_date,
            "precision": decimal_precision
        }

        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        if data:
            return data
        else:
            return response.status_code

    def coins_chart_historical_interval(self, coin_id, vs_currency, num_days_ago, interval, decimal_precision="2"):
        '''
        @brief Retrieves historical market data for a specific coin within an interval.
        @param coin_id The ID of the coin.
        @param vs_currency The target currency for exchange rates.
        @param num_days_ago The number of days ago to retrieve data for.
        @param interval The data interval.
        @param decimal_precision The precision of the data.
        @return The historical market data in JSON format if successful, otherwise the status code.
        '''
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": vs_currency,
            "days": num_days_ago,
            "interval": interval,
            "precision": decimal_precision
        }

        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        if data:
            return data
        else:
            return response.status_code

    def exchanges_chart_volume(self, coin_id, num_days_ago):
        '''
        @brief Retrieves exchange volume data for a specific coin.
        @param coin_id The ID of the coin.
        @param num_days_ago The number of days ago to retrieve data for.
        @return The exchange volume data in JSON format if successful, otherwise the status code.
        '''
        url = f"https://api.coingecko.com/api/v3/exchanges/{coin_id}/volume_chart"
        params = {
            "days": num_days_ago
        }

        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        if data:
            return data
        else:
            return response.status_code

    def coins_chart_OHLC(self, coin_id, vs_currency, num_days_ago, decimal_precision="2"):
        '''
        @brief Retrieves OHLC (Open, High, Low, Close) data for a specific coin.
        @param coin_id The ID of the coin.
        @param vs_currency The target currency for exchange rates.
        @param num_days_ago The number of days ago to retrieve data for.
        @param decimal_precision The precision of the data.
        @return The OHLC data in JSON format if successful, otherwise the status code.
        '''
        url = f"https://api.coingecko.com/api/v3/exchanges/{coin_id}/volume_chart"
        params = {
            "vs_currency": vs_currency,
            "days": num_days_ago,
            "precision": decimal_precision
        }

        response = requests.get(url, headers=self._headers, params=params)
        data = response.json()

        if data:
            return data
        else:
            return response.status_code

if __name__ == "__main__":
    '''
    @brief Tests the API key and CoinGecko server status without the class.
    '''
    testMarket = PyCT("CG-aTnmuupTErMjud8p9vbPqVYS")
    print(testMarket.ping_API_server())