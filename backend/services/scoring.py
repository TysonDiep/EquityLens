def get_rating(score):
    if score >= 80:
        return "Excellent"
    elif score >= 65:
        return "Good"
    elif score >= 50:
        return "Fair"
    elif score >= 35:
        return "Weak"
    else:
        return "Poor"

def score_growth(revenue_growth, eps_growth):
    score = 50
    reasons = []

    if revenue_growth is not None:
        if revenue_growth >= 20:
            score += 25
            reasons.append(f"Revenue grew {revenue_growth:.1f}%, which is excellent.")
        elif revenue_growth >= 10:
            score += 15
            reasons.append(f"Revenue grew {revenue_growth:.1f}%, which is strong.")
        elif revenue_growth >= 5:
            score += 5
            reasons.append(f"Revenue grew {revenue_growth:.1f}%, which is positive.")
        elif revenue_growth < 0:
            score -= 20
            reasons.append(f"Revenue declined {abs(revenue_growth):.1f}%.")
        else:
            reasons.append(f"Revenue growth was limited at {revenue_growth:.1f}%.")

    if eps_growth is not None:
        if eps_growth >= 20:
            score += 25
            reasons.append(f"EPS grew {eps_growth:.1f}%, which is excellent.")
        elif eps_growth >= 10:
            score += 15
            reasons.append(f"EPS grew {eps_growth:.1f}%, which is strong.")
        elif eps_growth >= 5:
            score += 5
            reasons.append(f"EPS grew {eps_growth:.1f}%, which is positive.")
        elif eps_growth < 0:
            score -= 20
            reasons.append(f"EPS declined {abs(eps_growth):.1f}%.")
        else:
            reasons.append(f"EPS growth was limited at {eps_growth:.1f}%.")

    score = max(0, min(score, 100))

    return {
        "score": score,
        "rating": get_rating(score),
        "reason": " ".join(reasons)
    }


def score_profitability(net_income_growth):
    score = 50
    reasons = []

    if net_income_growth is not None:
        if net_income_growth >= 20:
            score += 40
            reasons.append(
                f"Net income grew {net_income_growth:.1f}%, which is excellent."
            )
        elif net_income_growth >= 10:
            score += 25
            reasons.append(
                f"Net income grew {net_income_growth:.1f}%, which is strong."
            )
        elif net_income_growth >= 5:
            score += 10
            reasons.append(
                f"Net income grew {net_income_growth:.1f}%, which is positive."
            )
        elif net_income_growth < 0:
            score -= 30
            reasons.append(
                f"Net income declined {abs(net_income_growth):.1f}%."
            )
        else:
            reasons.append(
                f"Net income growth was limited at {net_income_growth:.1f}%."
            )

    else:
        reasons.append("Net income growth data is unavailable.")

    score = max(0, min(score, 100))

    return {
        "score": score,
        "rating": get_rating(score),
        "reason": " ".join(reasons)
    }

def score_valuation(pe_ratio, peg_ratio):
    score = 50
    reasons = []

    if pe_ratio is not None:
        if pe_ratio < 15:
            score += 20
            reasons.append(
                f"P/E ratio is {pe_ratio:.1f}, which is relatively low."
            )
        elif pe_ratio < 25:
            score += 10
            reasons.append(
                f"P/E ratio is {pe_ratio:.1f}, which is reasonable."
            )
        elif pe_ratio > 50:
            score -= 20
            reasons.append(
                f"P/E ratio is {pe_ratio:.1f}, which is very high."
            )
        elif pe_ratio > 35:
            score -= 10
            reasons.append(
                f"P/E ratio is {pe_ratio:.1f}, which is elevated."
            )
        else:
            reasons.append(
                f"P/E ratio is {pe_ratio:.1f}, which is moderately valued."
            )
    else:
        reasons.append("P/E ratio is unavailable.")

    if peg_ratio is not None:
        if peg_ratio < 1:
            score += 30
            reasons.append(
                f"PEG ratio is {peg_ratio:.1f}, suggesting the stock may be undervalued relative to growth."
            )
        elif peg_ratio < 2:
            score += 15
            reasons.append(
                f"PEG ratio is {peg_ratio:.1f}, which is reasonable relative to growth."
            )
        elif peg_ratio > 3:
            score -= 20
            reasons.append(
                f"PEG ratio is {peg_ratio:.1f}, which is very high."
            )
        elif peg_ratio > 2:
            score -= 10
            reasons.append(
                f"PEG ratio is {peg_ratio:.1f}, which is elevated."
            )
        else:
            reasons.append(
                f"PEG ratio is {peg_ratio:.1f}, which is moderately valued."
            )
    else:
        reasons.append("PEG ratio is unavailable.")

    score = max(0, min(score, 100))

    return {
        "score": score,
        "rating": get_rating(score),
        "reason": " ".join(reasons)
    }

def score_financial_health(free_cash_flow):
    if free_cash_flow is None:
        return {
            "score": 50,
            "rating": get_rating(50),
            "reason": "Free cash flow data is unavailable."
        }

    if free_cash_flow > 0:
        return {
            "score": 75,
            "rating": get_rating(75),
            "reason": f"The company generates positive free cash flow of ${free_cash_flow:,.0f}."
        }

    return {
        "score": 25,
        "rating": get_rating(25),
        "reason": f"The company has negative free cash flow of ${abs(free_cash_flow):,.0f}."
    }
    

def combine_financial_health_scores(
    free_cash_flow_score,
    balance_sheet_score
):
    if free_cash_flow_score is None and balance_sheet_score is None:
        return {
            "score": 50,
            "rating": get_rating(50),
            "reason": "Financial health data is unavailable."
        }

    if free_cash_flow_score is None:
        final_score = balance_sheet_score

    elif balance_sheet_score is None:
        final_score = free_cash_flow_score

    else:
        final_score = round(
            free_cash_flow_score * 0.60
            + balance_sheet_score * 0.40
        )

    return {
        "score": final_score,
        "rating": get_rating(final_score),
        "reason": (
            f"Financial health combines free cash flow strength "
            f"and balance-sheet strength. "
            f"Free cash flow score: {free_cash_flow_score}. "
            f"Balance-sheet score: {balance_sheet_score}."
        )
    }

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


def score_balance_sheet(current_ratio, debt_to_equity, net_debt):
    score = 50
    reasons = []

    # Current ratio
    if current_ratio is not None:
        if current_ratio >= 2:
            score += 15
            reasons.append(
                f"Current ratio is {current_ratio:.2f}, indicating strong short-term liquidity."
            )
        elif current_ratio >= 1:
            score += 5
            reasons.append(
                f"Current ratio is {current_ratio:.2f}, indicating adequate short-term liquidity."
            )
        else:
            score -= 15
            reasons.append(
                f"Current ratio is {current_ratio:.2f}, indicating weaker short-term liquidity."
            )

    # Debt-to-equity
    if debt_to_equity is not None:
        if debt_to_equity < 0.25:
            score += 15
            reasons.append(
                f"Debt-to-equity is {debt_to_equity:.2f}, indicating low leverage."
            )
        elif debt_to_equity < 0.75:
            score += 5
            reasons.append(
                f"Debt-to-equity is {debt_to_equity:.2f}, indicating moderate leverage."
            )
        elif debt_to_equity > 1:
            score -= 15
            reasons.append(
                f"Debt-to-equity is {debt_to_equity:.2f}, indicating high leverage."
            )
        else:
            reasons.append(
                f"Debt-to-equity is {debt_to_equity:.2f}."
            )

    # Net debt
    if net_debt is not None:
        if net_debt < 0:
            score += 15
            reasons.append(
                "The company has more cash and investments than debt."
            )
        elif net_debt > 0:
            reasons.append(
                "The company has more debt than cash and investments."
            )

    score = max(0, min(score, 100))

    return {
        "score": score,
        "rating": get_rating(score),
        "reason": " ".join(reasons)
    }