import json

f = open('coin_names.json',)

coin_names = json.load(f)

coin_array = []

for key, value in coin_names.items():
    coin_array.append((key, value))

print(coin_array[:1000])
