def sma(data, p):
    return [None if i<p else sum(data[i-p:i])/p for i in range(len(data))]

def rsi(c, p=14):
    g=l=0
    for i in range(-p,-1):
        d=c[i+1]-c[i]
        g+=max(d,0); l+=max(-d,0)
    rs=g/(l or 1)
    return 100-(100/(1+rs))

def fibo(h,l):
    return {
        "tp1": round(h-(h-l)*0.382,0),
        "tp2": round(h-(h-l)*0.236,0),
        "sl": round(h-(h-l)*0.786,0)
    }
