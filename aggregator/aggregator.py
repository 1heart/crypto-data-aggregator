import ccxt
import json
import time
import unicodecsv as csv
from datetime import datetime


#hitbtc = ccxt.hitbtc({'verbose': True})
#bitmex = ccxt.bitmex()
#binance = ccxt.binance()
exchanges = {'coinmarketcap': ccxt.coinmarketcap(), 'binance': ccxt.binance(), 'bitmex': ccxt.bitmex(), 
'bitfinex': ccxt.bitfinex(), 'kraken': ccxt.kraken(), 'kucoin': ccxt.kucoin(), 'hitbtc': ccxt.hitbtc({'verbose': True})}


with open('ccxt_data.csv', 'wb') as outfile:
	fieldnames = ["exchange", "symbol", "data"]
	schreiber = csv.DictWriter(outfile,fieldnames=fieldnames, encoding='utf-8')
	#schreiber.writeheader()

	for name, ex in exchanges.items():
		exchange = ex
		exchange.load_markets()
		if exchange.has['fetchOHLCV']:
		    for symbol in exchange.markets:
		        time.sleep (exchange.rateLimit / 1000) # time.sleep wants second

		        data = [exchange.fetch_ohlcv(symbol, '1d')]
		        schreiber.writerow({"exchange": name, "symbol": symbol, "data": data})

	        
	        # with open(name + '_' + '_data.txt', 'w') as outfile:
	        # 	json.dump(data, outfile)


# exchange = ccxt.binance() # default id
# print(exchange.load_markets())





# etheur1 = exchange.markets['ETH/BTC']      # get market structure by symbol
# # etheur2 = exchange.market ('ETHBTC')      # same result in a slightly different way

# etheurId = exchange.market_id ('BTC/USD')  # get market id by symbol

# symbols = exchange.symbols                 # get a list of symbols
# symbols2 = list (exchange.markets.keys ()) # same as previous line

# print (exchange.id, symbols)               # print all symbols



#print(binance.symbols)

# for ticker in binance.symbols:
# 	if ticker == 'ETH/BTC' or ticker == 'LTC/BTC':
# 		print(ticker)


# coinmarketcap=ccxt.coinmarketcap()
# coinmarketcap.load_markets()
# print(coinmarketcap.market('BTC/USD'))
# print(coinmarketcap.market('ETH/USD'))

# print(coinmarketcap.fetch_ticker('BTC/USD'))
# print(coinmarketcap.fetch_ticker('ETH/USD'))
# print(coinmarketcap.fetch_ticker('LTC/USD'))




#gdax = ccxt.gdax()

#huobi  = ccxt.huobi()
# exmo   = ccxt.exmo({
#     'apiKey': 'YOUR_PUBLIC_API_KEY',
#     'secret': 'YOUR_SECRET_PRIVATE_KEY',
# })

#hitbtc_markets = hitbtc.load_markets()



#print(hitbtc.id, hitbtc_markets)
#print(bitmex.id, bitmex.load_markets())
#print(coinmarketcap.id, coinmarketcap.load_markets())
#print(coinmarketcap.ticker(start=0,limi=3))
#print(gdax.id, gdax.load_markets())

#print(huobi.id, huobi.load_markets())

# print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
# print(bitmex.fetch_ticker('BTC/USD'))
#print(huobi.fetch_trades('LTC/CNY'))

# print(exmo.fetch_balance())

# # sell one ฿ for market price and receive $ right now
# print(exmo.id, exmo.create_market_sell_order('BTC/USD', 1))

# # limit buy BTC/EUR, you pay €2500 and receive ฿1  when the order is closed
# print(exmo.id, exmo.create_limit_buy_order('BTC/EUR', 1, 2500.00))

# pass/redefine custom exchange-specific order params: type, amount, price, flags, etc...
# kraken.create_market_buy_order('BTC/USD', 1, {'trading_agreement': 'agree'})