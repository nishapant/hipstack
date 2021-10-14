import pandas as pd
from random import seed
from random import randint


file_names = ['coin_Bitcoin.csv', 'coin_Cosmos.csv', 'coin_Dogecoin.csv', 'coin_Ethereum.csv',
                'coin_Litecoin.csv', 'coin_Tether.csv', 'coin_USDCoin.csv', 'coin_Solana.csv']

indices = [435, 806, 1077, 1264, 1996, 3216, 3361, 3027]

coin_info = []


for i in range(len(file_names)):
    df = pd.read_csv (file_names[i])

    curr_index = indices[i]
    seed(1)
    for index, entry in df.iterrows():
        date = entry['Date']
        high = entry['High']
        low = entry['Low']
        open_ = entry['Open']
        close = entry['Close']
        volume = entry['Volume']
        marketcap = entry['Marketcap']
        coinid = curr_index
        sentiment = randint(-1, 1)


        coin_info.append([date, open_, close, high, low, volume, marketcap, sentiment, coinid])


df2 = pd.DataFrame(coin_info, columns=['TradingDate', 'TradingOpen', 'TradingClose', 'TradingHigh', 'TradingLow', 'TradingVolume', 
    'TradingMarketCap', 'OverallSentiment', 'CoinID'])

print(df2)

df2.to_csv('past_daily.csv')
