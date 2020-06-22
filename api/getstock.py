from flask import request
import yfinance as yf
import json
import pandas as pd

class stock:

    def __init__(self):
        self.ticker = ''
        self.info = ''
        self.df = ''
        self.choice = ''

    def get_stock(self):
        self.choice = request.form['ticker']
        self.ticker = yf.Ticker(self.choice)
        self.info = self.ticker.history(period='1d')
        self.df = self.info
        self.df.reset_index(inplace=True)
        return(json.loads(self.df.to_json(orient='index')))
        


