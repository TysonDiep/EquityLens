from backend.services.financialanalysis import (
    calculate_growth,
    analyze_financials,
    calculate_free_cash_flow,
    calculate_eps_growth,
    analyze_balance_sheet,
)


def test_calculate_growth_with_zero_previous():
    result = calculate_growth(100, 0)

    assert result is None


def test_analyze_financials_with_empty_data():
    result = analyze_financials([])

    assert result is None


def test_free_cash_flow_with_missing_data():
    data = [
        {
            "operatingCashFlow": 1000,
            "capitalExpenditure": None,
        }
    ]

    result = calculate_free_cash_flow(data)

    assert result is None


def test_eps_growth_with_insufficient_history():
    data = [
        {
            "eps": 5
        }
    ]

    result = calculate_eps_growth(data)

    assert result is None


def test_eps_growth_with_missing_eps():
    data = [
        {
            "eps": 5
        },
        {
            "eps": None
        }
    ]

    result = calculate_eps_growth(data)

    assert result is None

    
def test_analyze_balance_sheet():
    data = [
        {
            "cashAndCashEquivalents": 5_539_000_000,
            "shortTermInvestments": 5_013_000_000,
            "totalDebt": 4_472_000_000,
            "totalCurrentAssets": 26_947_000_000,
            "totalCurrentLiabilities": 9_455_000_000,
            "totalLiabilities": 13_927_000_000,
            "totalEquity": 62_999_000_000,
        }
    ]

    result = analyze_balance_sheet(data)

    assert result["cash_and_investments"] == 10_552_000_000
    assert result["total_debt"] == 4_472_000_000
    assert result["net_debt"] == -6_080_000_000
    assert round(result["current_ratio"], 2) == 2.85
    assert round(result["debt_to_equity"], 3) == 0.071


def test_analyze_balance_sheet_with_empty_data():
    result = analyze_balance_sheet([])
    assert result is None


def test_analyze_balance_sheet_with_zero_denominators():
    data = [
        {
            "cashAndCashEquivalents": 1000,
            "shortTermInvestments": 500,
            "totalDebt": 200,
            "totalCurrentAssets": 5000,
            "totalCurrentLiabilities": 0,
            "totalLiabilities": 1000,
            "totalEquity": 0,
        }
    ]

    result = analyze_balance_sheet(data)

    assert result["cash_and_investments"] == 1500
    assert result["net_debt"] == -1300
    assert result["current_ratio"] is None
    assert result["debt_to_equity"] is None