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
