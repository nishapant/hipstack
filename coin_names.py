import json
import pandas as pd
from random import seed
from random import randint

f = open('coin_names.json',)
seed(1)
coin_names = json.load(f)
coin_array = []

for key, value in coin_names.items():
    sentiment = randint(-1, 1)
    coin_array.append([value, key, sentiment])

df = pd.DataFrame(coin_array, columns = ['CoinName', 'CoinDisplay', 'Sentiment'])

df.to_csv('coins.csv')

