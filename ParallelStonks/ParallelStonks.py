import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import yahoofinancials as yahoof
import datetime as date

#Using yahoofinancials
today = date.datetime.today()

# Get the data for the stock Tesla by specifying the stock ticker, start date, and end date
yahoo_financials = yahoof.YahooFinancials('TSLA')
data = yahoo_financials.get_historical_price_data(start_date='2015-01-01', 
                                                  end_date='2020-01-01', 
                                                  time_interval='daily')

# Create pandas datframe and format
tsla_df = pd.DataFrame(data['TSLA']['prices'])
tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
tsla_df_close = tsla_df['close']

# Print test
print(tsla_df.head())
print(tsla_df.shape)
print(tsla_df_close)

# Plot the close price
tsla_df_close.plot()
plt.show()
