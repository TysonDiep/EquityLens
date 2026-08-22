from fastapi import APIRouter, HTTPException

from services.marketdata import get_profile, get_quote

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