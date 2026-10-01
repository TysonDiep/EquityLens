from backend.services.financialanalysis import (
    calculate_growth,
    analyze_financials,
    calculate_free_cash_flow,
    calculate_eps_growth,
    analyze_balance_sheet,
    calculate_historical_growth,
    analyze_growth_trend,
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
    
    
def test_calculate_historical_growth():
    statements = [
        {"date": "2025-12-27", "revenue": 130},
        {"date": "2024-12-28", "revenue": 100},
        {"date": "2023-12-30", "revenue": 80},
    ]

    result = calculate_historical_growth(statements, "revenue")

    assert result[0]["year"] == "2025-12-27"
    assert result[0]["growth"] == 30

    assert result[1]["year"] == "2024-12-28"
    assert result[1]["growth"] == 25
    
    
def test_analyze_growth_trend_consistent():
    historical_growth = [
        {"year": "2025", "growth": 30},
        {"year": "2024", "growth": 20},
        {"year": "2023", "growth": 10},
    ]

    result = analyze_growth_trend(historical_growth)

    assert result["trend"] == "Consistent"
    assert result["average_growth"] == 20


def test_analyze_growth_trend_improving():
    historical_growth = [
        {"year": "2025", "growth": 30},
        {"year": "2024", "growth": 10},
        {"year": "2023", "growth": -5},
    ]

    result = analyze_growth_trend(historical_growth)

    assert result["trend"] == "Improving"


def test_analyze_growth_trend_declining():
    historical_growth = [
        {"year": "2025", "growth": -5},
        {"year": "2024", "growth": 10},
        {"year": "2023", "growth": 30},
    ]

    result = analyze_growth_trend(historical_growth)

    assert result["trend"] == "Declining"


def test_analyze_growth_trend_volatile():
    historical_growth = [
        {"year": "2025", "growth": 30},
        {"year": "2024", "growth": -10},
        {"year": "2023", "growth": 25},
    ]

    result = analyze_growth_trend(historical_growth)

    assert result["trend"] == "Improving"


def test_analyze_growth_trend_unavailable():
    result = analyze_growth_trend([])

    assert result["trend"] == "Unavailable"
    assert result["average_growth"] is None
    
    
def test_analyze_growth_trend_volatile():
    historical_growth = [
        {"year": "2025", "growth": 30},
        {"year": "2024", "growth": -10},
        {"year": "2023", "growth": 25},
    ]

    result = analyze_growth_trend(historical_growth)

    assert result["trend"] == "Volatile"   