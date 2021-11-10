import random
from app import db

def query_name():
	return random.choice(["BTC", "ETH", "MPL", "Z2O"])

def all_coins() -> dict:
# just to make sure interface displays data correctly
	Coins = [
		{
			"coinID": 1,
			"CoinName": "Bitcoin",
			"CoinDisplay": "BTC",
			"OverallSentiment": 70.2
		},

		{
			"coinID": 2,
			"CoinName": "Ethereum",
			"CoinDisplay": "ETH",
			"OverallSentiment": 59.4
		},

		{
			"coinID": 3,
			"CoinName": "Wonderland",
			"CoinDisplay": "TIME",
			"OverallSentiment": 288.6
		},


	]

	return Coins

def fetch_coins() -> dict:

    conn = db.connect()
    query_results = conn.execute("Select * from Coins;").fetchall()
    conn.close()
    coin_list = []
    for result in query_results:
        item = {
            "coinID": result[0],
            "CoinName": result[1],
            "CoinDisplay": result[2],
            "OverallSentiment": result[3]
        }
        coin_list.append(item)

    return coin_list


def update_coin_entry(coinID: int, CoinName: str, CoinDisplay: str, OverallSentiment: float) -> None:
# not tested yet
    conn = db.connect()
    query = 'Update Coins set CoinName = "{}", CoinDisplay = "{}", OverallSentiment = {} where id = {};'.format(CoinName, CoinDisplay, OverallSentiment, coinID)
    conn.execute(query)
    conn.close()

def insert_new_coin(CoinName: str, CoinDisplay: str, OverallSentiment: float) ->  int:

    conn = db.connect()
    query = 'Insert Into Coins (CoinName, CoinDisplay, OverallSentiment) VALUES ("{}", "{}", {});'.format(
        CoinName, CoinDisplay, OverallSentiment)
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    coinID = query_results[0][0]
    conn.close()

    return coinID



def removecoinbyid(coinID: int) -> None:
    conn = db.connect()
    query = 'Delete From Coins where id={};'.format(coinID)
    conn.execute(query)
    conn.close()

def keywordsearch(text: str) -> None:
    conn = db.connect()
    query = 'Select * from Coins where CoinName LIKE "%{}%" OR CoinDisplay LIKE "%{}%"'.format(text, text)
    query_results = conn.execute(query).fetchall()
    conn.close()
    coin_list = []
    for result in query_results:
        item = {
            "coinID": result[0],
            "CoinName": result[1],
            "CoinDisplay": result[2],
            "OverallSentiment": result[3]
        }
        coin_list.append(item)

    return coin_list

def yearhighestall() -> None:
    # lead this to another endpt with just a table, can do that for other queries too
    conn = db.connect()
    query = 'SELECT c1.CoinID, c1.CoinName, p.TradingDate, SQ.YearsHighest FROM Coin c1 JOIN PastDaily p ON c1.CoinID = p.CoinID JOIN (SELECT c2.CoinID, MAX(p.TradingHigh) as YearsHighest FROM Coin c2 JOIN PastDaily p ON c2.CoinID = p.CoinID GROUP BY c2.CoinID) AS SQ on SQ.CoinID = c1.CoinID WHERE p.TradingDate >= NOW() - INTERVAL 365 DAY AND p.TradingHigh = SQ.YearsHighest LIMIT 15;'
    query_results = conn.execute(query).fetchall()
    conn.close()
    coin_list = []
    for result in query_results:
        item = {
            "coinID": result[0],
            "CoinName": result[1],
            "TradingDate": result[2],
            "YearsHighest": result[3]
        }
        coin_list.append(item)

    return coin_list


def avgsentvalueall() -> None:
    # lead this to another endpt with just a table, can do that for other queries too
    conn = db.connect()
    query = 'SELECT c.CoinID, c.CoinName, AVG(h.OverallSentiment) as AvgOverallSentiment, AVG(h.TradingValue) as AvgTradingValue FROM Coin c JOIN HourOf h on h.CoinID = c.CoinID GROUP BY CoinID ORDER BY AvgOverallSentiment, AvgTradingValue LIMIT 15;'
    query_results = conn.execute(query).fetchall()
    conn.close()
    coin_list = []
    for result in query_results:
        item = {
            "coinID": result[0],
            "CoinName": result[1],
            "AvgSentiment": result[2],
            "AvgValue": result[3]
        }
        coin_list.append(item)

    return coin_list





