from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app import database as db

@app.route("/delete/<int:coinID>", methods=['POST'])
def delete(coinID):
    """ recieved post requests for entry delete """

    try:
        db.removebycoinid(coinID)
        result = {'success': True, 'response': 'Removed coin'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/update/<int:coinID>", methods=['POST'])
def update(coinID):
    """ recieved post requests for entry updates """

    data = request.get_json()
	# handle nulls in update function
    # print(coinID)
    # print(data)
    try:
        db.update_coin_entry(coinID, data["CoinName"], data["CoinDisplay"], data["OverallSentiment"])
        result = {'success': True, 'response': 'Coin updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    # print(data)
    db.insert_new_coin(data["CoinName"], data["CoinDisplay"], data["OverallSentiment"])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
	# switch for database testing
	items = db.all_coins()
	# items = db.fetch_coins()
	return render_template("index.html", items=items)

@app.route("/search/<string:input>")
def searchresult(input):
	# switch for database testing
	# items = db.all_coins()
	# print(input)
	items = db.keywordsearch(input)
	# print(items)
	# page not rendering, for now test by going directly to /search/input
	return render_template("searchresult.html", items=items)

@app.route("/yearhighest")
def yearhighest():
	# switch for database testing
	# items = db.all_coins()
	items = db.yearhighestall()
	return render_template("yearhighest.html", items=items)

@app.route("/avgsentvalue")
def avgsentvalue():
	# switch for database testing
	# items = db.all_coins()
	items = db.avgsentvalueall()
	return render_template("avgsentvalue.html", items=items)



