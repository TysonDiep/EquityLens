def calculate_growth(current, previous):
    if previous == 0:
        return None

    return ((current - previous) / previous) * 100

def analyze_financials(income_statements):
    if not income_statements:
        return None

    current = income_statements[0]

    analysis = {
        "revenue": current.get("revenue"),
        "gross_profit": current.get("grossProfit"),
        "operating_income": current.get("operatingIncome"),
        "net_income": current.get("netIncome"),
        "eps": current.get("eps")
    }

    if len(income_statements) > 1:
        previous = income_statements[1]

        analysis["revenue_growth"] = calculate_growth(
            current.get("revenue"),
            previous.get("revenue")
        )

        analysis["net_income_growth"] = calculate_growth(
            current.get("netIncome"),
            previous.get("netIncome")
        )

    return analysis

def calculate_free_cash_flow(cash_flow_statement):
    if not cash_flow_statement:
        return None

    current = cash_flow_statement[0]

    operating_cash_flow = current.get("operatingCashFlow")
    capital_expenditure = current.get("capitalExpenditure")

    if operating_cash_flow is None or capital_expenditure is None:
        return None

    return operating_cash_flow + capital_expenditure

def calculate_eps_growth(income_statements):
    if len(income_statements) < 2:
        return None

    current_eps = income_statements[0].get("eps")
    previous_eps = income_statements[1].get("eps")

    if current_eps is None or previous_eps is None:
        return None

    if previous_eps == 0:
        return None

    return calculate_growth(current_eps, previous_eps)