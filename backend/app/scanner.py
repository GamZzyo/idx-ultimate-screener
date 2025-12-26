import yfinance as yf
from indicators import sma, rsi, fibo

TICKERS=["BBCA.JK","BBRI.JK","BMRI.JK","TLKM.JK","ANTM.JK"]

def scan_all():
    res=[]
    for t in TICKERS:
        df=yf.download(t,period="6mo",progress=False)
        close_series = df["Close"]

# jika Close berupa DataFrame (multi-index), ambil kolom pertama
if hasattr(close_series, "columns"):
    close_series = close_series.iloc[:, 0]

c = close_series.dropna().to_list()
        if len(c)<60: continue
        ma20=sma(c,20); ma50=sma(c,50)
        f=fibo(max(c),min(c))
        score=(50 if ma20[-1]>ma50[-1] else 0)+(30 if rsi(c)<70 else 0)
        res.append({
            "ticker":t.replace(".JK",""),
            "trend":"Bullish" if ma20[-1]>ma50[-1] else "Bearish",
            "rsi":round(rsi(c),1),
            "tp1":f["tp1"],
            "tp2":f["tp2"],
            "sl":f["sl"],
            "score":score
        })
    return sorted(res,key=lambda x:x["score"],reverse=True)
