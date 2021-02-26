import finviz as fv
filters = ['exch_nasd', 'idx_sp500']
stock_list = fv.Screener(filters = filters, table = 'Performance', order = 'price')
print(stock_list)

stock = fv.get_stock('AAPL')
print(stock['Price'])
