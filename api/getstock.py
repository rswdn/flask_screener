import yfinance as yf

class stock:

    def __init__(self):
        self.ticker = ''
        self.info = ''

    def get_stock(self):
        self.ticker = yf.Ticker("TSLA")

        self.info = self.ticker.history(period='1d')

        return(self.info)




