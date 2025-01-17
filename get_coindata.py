#! /usr/bin/env python3
import requests

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
response = requests.get(URL)
if response.status_code == 200:
        data = response.json()
        for coin in data:
                print(f"Name: {coin['name']}, Price: {coin['current_price']}")
else:
        print("Error Fetching Data:", response.status_code)
