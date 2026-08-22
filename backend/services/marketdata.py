import os

import requests
from dotenv import load_dotenv

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")


def get_quote(symbol: str):
    url = "https://financialmodelingprep.com/stable/quote"

    params = {
        "symbol": symbol.upper(),
        "apikey": FMP_API_KEY
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    if not data:
        return None

    return data[0]


def get_profile(symbol: str):
    url = "https://financialmodelingprep.com/stable/profile"

    params = {
        "symbol": symbol.upper(),
        "apikey": FMP_API_KEY
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    if not data:
        return None

    return data[0]