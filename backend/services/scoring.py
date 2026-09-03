def score_growth(revenue_growth, eps_growth):
    score = 50

    if revenue_growth is not None:
        if revenue_growth >= 20:
            score += 25
        elif revenue_growth >= 10:
            score += 15
        elif revenue_growth >= 5:
            score += 5
        elif revenue_growth < 0:
            score -= 20

    if eps_growth is not None:
        if eps_growth >= 20:
            score += 25
        elif eps_growth >= 10:
            score += 15
        elif eps_growth >= 5:
            score += 5
        elif eps_growth < 0:
            score -= 20

    return max(0, min(score, 100))


def score_profitability(net_income_growth):
    score = 50

    if net_income_growth is not None:
        if net_income_growth >= 20:
            score += 40
        elif net_income_growth >= 10:
            score += 25
        elif net_income_growth >= 5:
            score += 10
        elif net_income_growth < 0:
            score -= 30

    return max(0, min(score, 100))

def score_valuation(pe_ratio, peg_ratio):
    score = 50

    if pe_ratio is not None:
        if pe_ratio < 15:
            score += 20
        elif pe_ratio < 25:
            score += 10
        elif pe_ratio > 50:
            score -= 20
        elif pe_ratio > 35:
            score -= 10

    if peg_ratio is not None:
        if peg_ratio < 1:
            score += 30
        elif peg_ratio < 2:
            score += 15
        elif peg_ratio > 3:
            score -= 20
        elif peg_ratio > 2:
            score -= 10

    return max(0, min(score, 100))

def score_financial_health(free_cash_flow):
    if free_cash_flow is None:
        return 50

    if free_cash_flow > 0:
        return 75

    return 25

def calculate_equitylens_score(
    growth_score,
    profitability_score,
    financial_health_score,
    valuation_score
):
    score = (
        growth_score * 0.30
        + profitability_score * 0.25
        + financial_health_score * 0.20
        + valuation_score * 0.25
    )

    return round(score)