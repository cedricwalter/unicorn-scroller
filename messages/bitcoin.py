from pycoingecko import CoinGeckoAPI

# list of coins https://api.coingecko.com/api/v3/coins/list
price = CoinGeckoAPI().get_price(ids='bitcoin', vs_currencies='usd')

print 'colour:yellow'
print 'BTC ${}'.format(price['bitcoin']['usd'])