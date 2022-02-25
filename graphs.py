import numpy as np
import pandas as pd


#Data viz
import plotly.graph_objs as go

#import yfinance as yf
#data = yf.download(tickers='BTC-USD', period = '22h', interval = '15m')

def graa(data, timeP, timeI, cryptn):
    fig = go.Figure()

    #Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    # Add titles
    fig.update_layout(
        title=cryptn+' price evolution',
        yaxis_title=cryptn+' Price')

    # X-Axes


    #Show
    #fig.show()
    fig.write_image("dbot/dbimages/fig1.png")

#graa(data)
