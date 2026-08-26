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