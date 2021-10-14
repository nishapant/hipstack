import pandas as pd
from random import seed
from random import randint

df = pd.read_csv ('coin_Bitcoin.csv')

bitcoin = []

bitcoin_index = 435
seed(1)
for index, entry in df.iterrows():
    date = entry['Date']
    high = entry['High']
    low = entry['Low']
    open_ = entry['Open']
    close = entry['Close']
    volume = entry['Volume']
    marketcap = entry['Marketcap']
    coinid = bitcoin_index
    sentiment = randint(-1, 1)


    bitcoin.append([date, open_, close, high, low, volume, marketcap, sentiment, coinid])

df2 = pd.DataFrame(bitcoin, columns=['TradingDate', 'TradingOpen', 'TradingClose', 'TradingHigh', 'TradingLow', 'TradingVolume', 
'TradingMarketCap', 'OverallSentiment', 'CoinID'])

print(df2)
