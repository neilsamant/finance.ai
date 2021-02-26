import finviz as fv

# The getPrice function return the price of a stock defined by the string "ticker"
def getPrice(ticker):
    stock = fv.get_stock(ticker)
    price = stock['Price']
    return price


# The getList function returns the list of stock tickers (along with other information) for a 'exchanges' and sorted according to 'sort'
# sample exch (exchanges) - exch_nasd (NASDAQ), idx_sp500 (S&P500)
# sample sort (sorting order) - price (sort according to price)
def getList(exch, sort):
    stock_list = fv.Screener(filters = exch, table = 'Performance', order = sort)
    return stock_list