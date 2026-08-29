from fastapi import APIRouter, HTTPException

from services.marketdata import (
    get_balance_sheet,
    get_income_statement,
    get_profile,
    get_quote,
    get_cash_flow
)

from services.financialanalysis import (
    analyze_financials,
    calculate_free_cash_flow,
    calculate_eps_growth,
)


from services.valuations import analyze_valuation

router = APIRouter(
    prefix="/stock",
    tags=["Stocks"]
)


@router.get("/{symbol}")
def stock_quote(symbol: str):
    try:
        data = get_quote(symbol)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve stock data"
        )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Stock symbol '{symbol.upper()}' not found"
        )

    return data


@router.get("/{symbol}/profile")
def stock_profile(symbol: str):
    try:
        data = get_profile(symbol)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve company profile"
        )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Company '{symbol.upper()}' not found"
        )

    return data

@router.get("/{symbol}/financials")
def stock_financials(symbol: str):
    try:
        data = get_income_statement(symbol)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve financial data"
        )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Financial data for '{symbol.upper()}' not found"
        )

    return data

@router.get("/{symbol}/balance-sheet")
def stock_balance_sheet(symbol: str):
    try:
        data = get_balance_sheet(symbol)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve balance sheet"
        )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Balance sheet for '{symbol.upper()}' not found"
        )

    return data

@router.get("/{symbol}/cash-flow")
def stock_cash_flow(symbol: str):
    try:
        data = get_cash_flow(symbol)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve cash flow statement"
        )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Cash flow data for '{symbol.upper()}' not found"
        )

    return data

@router.get("/{symbol}/analysis")
def stock_analysis(symbol: str):
    try:
        financials = get_income_statement(symbol)
        analysis = analyze_financials(financials)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to analyze financial data"
        )

    if analysis is None:
        raise HTTPException(
            status_code=404,
            detail=f"Financial analysis for '{symbol.upper()}' not found"
        )
        
    return analysis

@router.get("/{symbol}/valuation")
def stock_valuation(symbol: str):
    try:
        quote = get_quote(symbol)
        income_statements = get_income_statement(symbol)
        cash_flow = get_cash_flow(symbol)

        if not quote or not income_statements or not cash_flow:
            raise HTTPException(
                status_code=404,
                detail=f"Valuation data for '{symbol.upper()}' not found"
            )

        current_financials = income_statements[0]
        eps_growth = calculate_eps_growth(income_statements)

        price = quote.get("price")
        market_cap = quote.get("marketCap")
        eps = current_financials.get("eps")
        revenue = current_financials.get("revenue")

        free_cash_flow = calculate_free_cash_flow(cash_flow)

        return analyze_valuation(
            price,
            market_cap,
            eps,
            revenue,
            free_cash_flow,
            eps_growth
        )

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to calculate valuation"
        )