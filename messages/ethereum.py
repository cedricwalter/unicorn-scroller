from pycoingecko import CoinGeckoAPI

# list of coins https://api.coingecko.com/api/v3/coins/list
price = CoinGeckoAPI().get_price(ids='ethereum', vs_currencies='usd')

print 'colour:grey'
print 'ETH ${}'.format(price['ethereum']['usd'])
