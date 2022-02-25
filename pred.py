import pandas as pd
from prophet import Prophet
import yfinance as yf
from datetime import datetime
from datetime import timedelta
import plotly.graph_objects as go
from prophet.plot import plot_plotly, plot_components_plotly


"""
cryptn, timeP, timeI = "BTC-INR", "24h", "15m"
data = yf.download(tickers=cryptn, period = timeP, interval = timeI)
#print(data.head())
#Datetime0   Open1        High2        Low3       Close4  Adj Close5       Volume6


df = pd.read_csv('dbexamp/example_wp_log_peyton_manning.csv')
df.head()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)

forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

"""

def predd(cryptn, start_date):
    today = datetime.today().strftime('%Y-%m-%d')
    eth_df = yf.download(cryptn,start_date, today)
    #print(eth_df.tail())
    #print(eth_df.info())
    eth_df.reset_index(inplace=True) #put date as index

    df = eth_df[["Date", "Open"]]
    new_names = {
        "Date": "ds",
        "Open": "y",
    }
    df.rename(columns=new_names, inplace=True)

    m = Prophet(
        #seasonality_mode="multiplicative",
        #mcmc_samples=300
        interval_width=0.95
    )
    m.fit(df)

    future = m.make_future_dataframe(periods = 5, freq = "D")

    forecast = m.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    #next_day = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    #return forecast[forecast['ds'] == next_day]['yhat'].item()

#print(predd("RVN-INR", "2016-01-01"))
