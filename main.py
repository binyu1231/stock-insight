import akshare as ak

## 个股 https://akshare.akfamily.xyz/data/stock/stock.html#id20
## Error
# stock_latest = ak.stock_individual_spot_xq(symbol="SPY")
# print(stock_latest)

## 日K
stock_daily = ak.stock_zh_a_hist(
  symbol = '601985', period = "daily", start_date = "20230401", end_date = "20240403"
)

print(stock_daily)