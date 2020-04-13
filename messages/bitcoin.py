from pycoingecko import CoinGeckoAPI
price = CoinGeckoAPI().get_price(ids='bitcoin', vs_currencies='usd')

print 'colour:yellow'
print 'BTC ${}'.format(price['bitcoin']['usd'])