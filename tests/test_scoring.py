from backend.services.scoring import (
    get_rating,
    score_growth,
    score_profitability,
    score_valuation,
    score_financial_health,
    calculate_equitylens_score,
    score_balance_sheet,
    combine_financial_health_scores,
)


def test_rating_excellent():
    assert get_rating(80) == "Excellent"
    assert get_rating(100) == "Excellent"


def test_rating_good():
    assert get_rating(65) == "Good"
    assert get_rating(79) == "Good"


def test_rating_fair():
    assert get_rating(50) == "Fair"
    assert get_rating(64) == "Fair"


def test_rating_weak():
    assert get_rating(35) == "Weak"
    assert get_rating(49) == "Weak"


def test_rating_poor():
    assert get_rating(0) == "Poor"
    assert get_rating(34) == "Poor"


def test_strong_growth():
    result = score_growth(20, 20)

    assert result["score"] == 100
    assert result["rating"] == "Excellent"


def test_negative_growth_is_penalized():
    result = score_growth(-10, -10)

    assert result["score"] == 10
    assert result["rating"] == "Poor"


def test_strong_profitability():
    result = score_profitability(20)

    assert result["score"] == 90
    assert result["rating"] == "Excellent"


def test_negative_profitability_is_penalized():
    result = score_profitability(-10)

    assert result["score"] == 20
    assert result["rating"] == "Poor"


def test_low_valuation():
    result = score_valuation(10, 0.8)

    assert result["score"] == 100
    assert result["rating"] == "Excellent"


def test_high_valuation_is_penalized():
    result = score_valuation(60, 4)

    assert result["score"] == 10
    assert result["rating"] == "Poor"


def test_positive_free_cash_flow():
    result = score_financial_health(1_000_000)

    assert result["score"] == 75
    assert result["rating"] == "Good"


def test_negative_free_cash_flow():
    result = score_financial_health(-1_000_000)

    assert result["score"] == 25
    assert result["rating"] == "Poor"


def test_equitylens_weighted_score():
    result = calculate_equitylens_score(
        growth_score=100,
        profitability_score=90,
        financial_health_score=75,
        valuation_score=45,
    )

    assert result == 79
    
def test_strong_balance_sheet():
    result = score_balance_sheet(
        current_ratio=2.85,
        debt_to_equity=0.071,
        net_debt=-6_080_000_000,
    )

    assert result["score"] == 95
    assert result["rating"] == "Excellent"


def test_adequate_balance_sheet():
    result = score_balance_sheet(
        current_ratio=1.5,
        debt_to_equity=0.5,
        net_debt=1_000_000_000,
    )

    assert result["score"] == 60
    assert result["rating"] == "Fair"


def test_weak_balance_sheet():
    result = score_balance_sheet(
        current_ratio=0.8,
        debt_to_equity=1.5,
        net_debt=5_000_000_000,
    )

    assert result["score"] == 20
    assert result["rating"] == "Poor"


def test_balance_sheet_missing_data():
    result = score_balance_sheet(
        current_ratio=None,
        debt_to_equity=None,
        net_debt=None,
    )

    assert result["score"] == 50
    assert result["rating"] == "Fair"
    

def test_combine_financial_health_scores():
    result = combine_financial_health_scores(
        free_cash_flow_score=75,
        balance_sheet_score=95,
    )

    assert result["score"] == 83
    assert result["rating"] == "Excellent"


def test_combine_financial_health_with_only_fcf():
    result = combine_financial_health_scores(
        free_cash_flow_score=75,
        balance_sheet_score=None,
    )

    assert result["score"] == 75
    assert result["rating"] == "Good"


def test_combine_financial_health_with_only_balance_sheet():
    result = combine_financial_health_scores(
        free_cash_flow_score=None,
        balance_sheet_score=95,
    )

    assert result["score"] == 95
    assert result["rating"] == "Excellent"


def test_combine_financial_health_with_no_data():
    result = combine_financial_health_scores(
        free_cash_flow_score=None,
        balance_sheet_score=None,
    )

    assert result["score"] == 50
    assert result["rating"] == "Fair"