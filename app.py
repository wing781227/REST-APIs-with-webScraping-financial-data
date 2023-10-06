from flask import Flask, request
from flask_smorest import abort
from yahoofinance import *
from db import stocks, news
import uuid


app = Flask(__name__)

@app.get("/stock")
def get_Allstocks():
    return stocks
    # return {"stocks": list(stocks.values())}

@app.post("/stock/<string:symbol>")
def fetch_stock(symbol):
    stocks[symbol] = getStockData(symbol)
    return stocks[symbol]
    # if symbol not in stocks:
    #     # temp = getStockData(symbol)
    #     # stocks[symbol, temp['current time']] = temp
    #     stocks[symbol] = getStockData(symbol)
    #     return stocks[symbol]
    # # return {'message': 'This company is in database already. Please try other options.'}
    # return abort(404, message='This company is in database already. Please try other options.')

@app.get("/news")
def get_Allnews():
    return news

# @app.get("/news/<string:symbol>")
# def get_news(symbol):
#     try:
#         return news[symbol]
#     except KeyError:
#         abort(404, message="This company is not in database!")

@app.post("/news/<string:symbol>")
def fetch_news(symbol):
    # if symbol not in stocks:
    #     # return {"message": "This company is not found in the database."}, 404
    #     return abort(404, message='This company is not found in the database.')
    news_data, data_uuid = getNewsData(symbol) 
    print("fetch_news",news_data)
    added_news = {**news_data}
    if symbol not in news:  
        # news[symbol][added_news['title']] = added_news['News_published_time'], added_news
        news[symbol] = {data_uuid: added_news}
    elif added_news['title'] not in news[symbol]:
        news[symbol] = {data_uuid: added_news}
    else:
        return abort(404, message='This news is in the database.')
    print(news)
    return added_news, 201 
    # return stocks[symbol]
    
@app.post("/news/<string:symbol>")
def manuallyInput_news(symbol):
    news_data = request.get_json()
    added_news = {**news_data}
    data_uuid = uuid.uuid4().hex
    if symbol not in news:  
        # news[symbol][added_news['title']] = added_news['News_published_time'], added_news
        news[symbol] = {data_uuid: added_news}
    elif added_news['title'] not in news[symbol]:
        news[symbol] = {data_uuid: added_news}
    else:
        return abort(404, message='This news is in the database.')
    print(news)
    return added_news, 201 
 
@app.delete("/news/<string:symbol>/<string:title>")
def delete_news(symbol, title):
    if title not in news[symbol]:
        return abort(404, message='This news is not in the database.')
    else:
        del news[symbol][title]
        return news