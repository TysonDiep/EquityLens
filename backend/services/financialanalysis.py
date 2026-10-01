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

def analyze_balance_sheet(balance_sheet):
    if not balance_sheet:
        return None

    current = balance_sheet[0]

    cash = current.get("cashAndCashEquivalents")
    short_term_investments = current.get("shortTermInvestments")
    total_debt = current.get("totalDebt")
    current_assets = current.get("totalCurrentAssets")
    current_liabilities = current.get("totalCurrentLiabilities")
    total_liabilities = current.get("totalLiabilities")
    total_equity = current.get("totalEquity")

    cash_and_investments = None

    if cash is not None and short_term_investments is not None:
        cash_and_investments = cash + short_term_investments

    net_debt = None

    if cash_and_investments is not None and total_debt is not None:
        net_debt = total_debt - cash_and_investments

    current_ratio = None

    if (
        current_assets is not None
        and current_liabilities is not None
        and current_liabilities != 0
    ):
        current_ratio = current_assets / current_liabilities

    debt_to_equity = None

    if (
        total_debt is not None
        and total_equity is not None
        and total_equity != 0
    ):
        debt_to_equity = total_debt / total_equity

    return {
        "cash_and_investments": cash_and_investments,
        "total_debt": total_debt,
        "net_debt": net_debt,
        "current_ratio": current_ratio,
        "debt_to_equity": debt_to_equity,
        "total_liabilities": total_liabilities,
        "total_equity": total_equity,
    }
    
def calculate_historical_growth(statements, field):
    if not statements:
        return []

    historical_growth = []

    for i in range(len(statements) - 1):
        current = statements[i].get(field)
        previous = statements[i + 1].get(field)

        growth = calculate_growth(current, previous)

        historical_growth.append({
            "year": statements[i].get("date"),
            "growth": growth
        })

    return historical_growth

def analyze_growth_trend(historical_growth):
    if not historical_growth:
        return {
            "trend": "Unavailable",
            "average_growth": None
        }

    growth_values = [
        item["growth"]
        for item in historical_growth
        if item["growth"] is not None
    ]

    if not growth_values:
        return {
            "trend": "Unavailable",
            "average_growth": None
        }

    average_growth = sum(growth_values) / len(growth_values)

    if all(growth >= 0 for growth in growth_values):
        trend = "Consistent"

    else:
        directions = []

        for i in range(len(growth_values) - 1):
            if growth_values[i] > growth_values[i + 1]:
                directions.append("down")
            elif growth_values[i] < growth_values[i + 1]:
                directions.append("up")

        if "up" in directions and "down" in directions:
            trend = "Volatile"

        elif growth_values[0] > growth_values[-1]:
            trend = "Improving"

        elif growth_values[0] < growth_values[-1]:
            trend = "Declining"

        else:
            trend = "Volatile"

    return {
        "trend": trend,
        "average_growth": average_growth
    }