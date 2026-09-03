import os

import requests
from dotenv import load_dotenv

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")


def make_fmp_request(endpoint: str, symbol: str):
    url = f"https://financialmodelingprep.com/stable/{endpoint}"

    params = {
        "symbol": symbol.upper().strip(),
        "apikey": FMP_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if not data:
        return None

    return data


def get_quote(symbol: str):
    data = make_fmp_request("quote", symbol)

    if not data:
        return None

    return data[0]


def get_profile(symbol: str):
    data = make_fmp_request("profile", symbol)

    if not data:
        return None

    return data[0]


def get_income_statement(symbol: str):
    return make_fmp_request("income-statement", symbol)


def get_balance_sheet(symbol: str):
    return make_fmp_request("balance-sheet-statement", symbol)


def get_cash_flow(symbol: str):
    return make_fmp_request("cash-flow-statement", symbol)