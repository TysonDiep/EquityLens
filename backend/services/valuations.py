def calculate_pe(price, eps):
    if price is None or eps is None or eps <= 0:
        return None

    return price / eps


def calculate_ps(market_cap, revenue):
    if market_cap is None or revenue is None or revenue <= 0:
        return None

    return market_cap / revenue


def calculate_pfcf(market_cap, free_cash_flow):
    if market_cap is None or free_cash_flow is None or free_cash_flow <= 0:
        return None

    return market_cap / free_cash_flow


def analyze_valuation(
    price,
    market_cap,
    eps,
    revenue,
    free_cash_flow,
    earnings_growth
):
    pe_ratio = calculate_pe(price, eps)

    return {
        "pe_ratio": pe_ratio,
        "price_to_sales": calculate_ps(market_cap, revenue),
        "price_to_free_cash_flow": calculate_pfcf(
            market_cap,
            free_cash_flow
        ),
        "peg_ratio": calculate_peg(
            pe_ratio,
            earnings_growth
        )
    }
    
def calculate_peg(pe_ratio, earnings_growth):
    if pe_ratio is None or earnings_growth is None:
        return None

    if earnings_growth <= 0:
        return None

    return pe_ratio / earnings_growth