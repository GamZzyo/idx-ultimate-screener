from fastapi import FastAPI
from app.scanner import scan_all

app=FastAPI(title="IDX Ultimate Screener")

@app.get("/scan")
def scan():
    return scan_all()
