import pandas as pd
import numpy as np
import yfinance as yf


def data_parse():

	symbol = ['MSFT','AAPL','GOOGL']
	df = yf.download(symbol,period='1d',interval='1m',group_by='ticker',auto_adjust=True)

	data1 = df[symbol[0]]
	data2 = df[symbol[1]]
	data3 = df[symbol[2]]

	return data1,data2,data3,symbol

