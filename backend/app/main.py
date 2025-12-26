from fastapi import FastAPI
from scanner import scan_all

app = FastAPI(title="IDX Ultimate Screener")

@app.get("/")
def root():
    return {
        "status": "OK",
        "message": "IDX Ultimate Screener API",
        "endpoint": "/scan"
    }
