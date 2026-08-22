from fastapi import FastAPI

from routes.stocks import router as stock_router


app = FastAPI(
    title="EquityLens",
    description="AI-assisted stock research and investment analysis platform",
    version="0.1.0"
)


app.include_router(stock_router)


@app.get("/")
def root():
    return {
        "message": "EquityLens API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }