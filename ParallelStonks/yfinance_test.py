import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import yahoofinancials as yahoof
import datetime as date

#Using yfinance 

tsla_df = yf.download('TSLA', 
                      start='2015-01-01', 
                      end='2020-01-01', 
                      progress=False)
tsla_df.head()

# Plot the close price
tsla_df['Close'].plot(title="TSLA's stock price")
plt.show()