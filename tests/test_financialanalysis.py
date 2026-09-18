from backend.services.financialanalysis import (
    calculate_growth,
    analyze_financials,
    calculate_free_cash_flow,
    calculate_eps_growth,
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