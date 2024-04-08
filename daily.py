import datetime
import akshare as ak
import pandas as pd

date = datetime.datetime.now().strftime("%Y-%m-%d")

def dailyA():

  # 京A: stock_bj_a_spot_em
  # 深A: stock_sz_a_spot_em
  # 沪A: stock_sh_a_spot_em
  stock = pd.DataFrame(ak.stock_zh_a_spot_em())

  stock.to_csv("dataSource/unhandled/A-{}.csv".format(date), index = False)



dailyA()