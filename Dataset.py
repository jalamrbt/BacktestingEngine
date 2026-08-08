import yfinance as yf
import pandas
class Dataset:
    def __init__(self,startDate,endDate,ticker,interval):
        self.startDate = startDate
        self.endDate = endDate
        self.ticker = ticker
        self.interval = interval

    def fetchData(self):
        self.data = yf.download(self.ticker,start = self.startDate,end =self.endDate,interval = self.interval)
        self.data.columns = self.data.columns.droplevel(1)

        
    

    