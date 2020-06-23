from flask import request,abort
import yfinance as yf
import json
import pandas as pd

class stock:

    def __init__(self):
        self.ticker = ''
        self.info = ''
        self.df = ''
        self.choice = ''
        self.result = ''

    def get_stock(self):
        self.choice = request.form['ticker'] #Requesting stock ticker
        self.ticker = yf.Ticker(self.choice) #Passing request through yf
        self.info = self.ticker.history(period='1d') #Setting history of stock, can be changed.
        self.df = self.info[['Close']] #setting results of request to DataFrame
        self.df.drop(self.df.columns[[1]], axis=1)
        self.df.reset_index(inplace=True)
        self.result = json.loads(self.df.to_json(orient='index'))

        if self.df.empty: #Checking if DataFrame is empty, if empty pass 404 error
            return abort(404, description="Ticker doesn't exist, please try again")
        else:#Else return DataFrame
            return self.result




        


