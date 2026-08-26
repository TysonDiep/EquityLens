from fastapi import APIRouter, HTTPException

from services.marketdata import (
    get_balance_sheet,
    get_income_statement,
    get_profile,
    get_quote,
    get_cash_flow
)

from services.financialanalysis import analyze_financials

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