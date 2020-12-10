from Thodex import ThodexClient

thdx = ThodexClient("apikey", "secret")

response = thdx.get_balance('BTC,ETC,TRY')
print(type(response))
print(response)

response = thdx.markets()
print(type(response))
print(response)

