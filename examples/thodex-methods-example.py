from Thodex import ThodexClient

thdx = ThodexClient("RmcZD7rG9HLsP5I1RyXOCGgkauvWI40XPepSnN6kYTjittycy2Qr2UCUXtt6CTJJ",
                    "tCgQyIUpDkdQc9pSNZPA4DXpmsLuUJ5L5HPOXR8wnSkcgWLhVY8rS2NhtBtPUzTc")

response = thdx.get_balance('BTC,ETC,TRY')
print(type(response))
print(response)

response = thdx.markets()
print(type(response))
print(response)

