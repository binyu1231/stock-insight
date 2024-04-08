import akshare as ak
import pandas as pd


def stock_history(code):

  stock_history = pd.DataFrame()

  stock = ak.stock_zh_a_hist(symbol = code)

  stock_history = pd.concat([stock])

  stock_history.to_csv("dataSource/{}.csv".format(code), index = False)


stock_history("601985")

print(stock_history)