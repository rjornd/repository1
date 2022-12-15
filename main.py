import pandas as pd
import pandas_datareader as web
import datetime as dt
import numpy as np
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def myRSI(price, n=20):
    delta = price['close'].diff()
    dUp, dDown = delta.copy(), delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0

    RolUp = dUp.rolling(window=n).mean()
    RolDown = dDown.rolling(window=n).mean().abs()
    
    RS = RolUp / RolDown
    rsi= 100.0 - (100.0 / (1.0 + RS))
    return rsi

if __name__ == "__main__":
    start = dt.datetime(2015,1,1)
    end = dt.datetime.now()
    df = web.DataReader("BTC-USD", "yahoo", start, end)
    print(df.head(10))

    df = df.rename(columns={'Open': 'open', 'Low': 'low', 'High': 'high', 'Close': 'close', 'Volume' : 'volume'})

    df=df[df['volume']!=0]

    df.isna().sum()
    df.head(10)
    df['RSI'] = df.ta.rsi(length=14)
    df.head(100)
    dfpl = df[-200:]
    fig = make_subplots(rows=2, cols=1)
    fig.append_trace(go.Candlestick(x=dfpl.index,
                    open=dfpl['open'],
                    high=dfpl['high'],
                    low=dfpl['low'],
                    close=dfpl['close']), row=1, col=1)
    fig.append_trace(go.Scatter(
        x=dfpl.index,
        y=dfpl['RSI'],
    ), row=2, col=1)

    fig.add_hline(y=30, row=2, col=1, line_dash="dash", line_color="green")
    fig.add_hline(y=60, row=2, col=1, line_dash="dash", line_color="red")
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()
    
    bought = False
    buyindex = 0
    scount = 0
    fcount = 0
    totalloss = 0
    totalprofit = 0
    for i in range(30,len(df)):
        if df.iloc[i]["RSI"] < 30: 
            if bought == False:
                print("Buy " + str(df.iloc[i].name))
                buyprice = df.iloc[i]['close']
                bought = True
                buyindex = i
        if bought and i == buyindex + 1:
            if buyprice >= df.iloc[i]['close']: 
                print("Fail")
                fcount+=1
                totalloss+= df.iloc[i]['close'] - buyprice
            else: 
                print("Success")
                scount+=1
                totalprofit+= df.iloc[i]['close'] - buyprice
            bought = False
    print("Winrate = " + str(scount/(scount+fcount)))
    print(totalprofit)
    print(totalloss)
    


