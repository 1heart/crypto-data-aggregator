import ccxt
import pdb


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Aggregate data from cryptocurrency exchanges.')
    parser.add_argument('--exchange', type=str, help='Exchange name for data, e.g. `binance`')
    args = parser.parse_args()

    exchanges = set(ccxt.exchanges)
    if args.exchange not in exchanges:
        raise KeyError('Exchange name not valid')

    exchange = getattr(ccxt, args.exchange)()
    if not exchange.has['fetchOHLCV']:
        raise NotImplementedError('Exchange does not support OHLCV (candlestick) charts')
    markets = exchange.load_markets()
    pdb.set_trace()
