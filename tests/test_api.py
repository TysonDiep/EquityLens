import sys
from pathlib import Path

from fastapi.testclient import TestClient


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from main import app


client = TestClient(app)


def test_amd_score_endpoint():
    response = client.get("/stock/AMD/score")

    assert response.status_code == 200

    data = response.json()

    assert data["symbol"] == "AMD"
    assert "growth" in data
    assert "profitability" in data
    assert "financial_health" in data
    assert "valuation" in data
    assert "equitylens_score" in data


def test_invalid_stock_symbol():
    response = client.get("/stock/NOTASTOCK")

    assert response.status_code == 404
    
def test_invalid_stock_profile():
    response = client.get("/stock/NOTASTOCK/profile")

    assert response.status_code == 404


def test_invalid_stock_financials():
    response = client.get("/stock/NOTASTOCK/financials")

    assert response.status_code == 404


def test_invalid_stock_balance_sheet():
    response = client.get("/stock/NOTASTOCK/balance-sheet")

    assert response.status_code == 404


def test_invalid_stock_cash_flow():
    response = client.get("/stock/NOTASTOCK/cash-flow")

    assert response.status_code == 404
    
def test_invalid_stock_score():
    response = client.get("/stock/NOTASTOCK/score")

    assert response.status_code == 200

    data = response.json()

    assert data["error"] == "Stock not found"
