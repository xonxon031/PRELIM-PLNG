
prices_usd = [10.0, 25.50, 4.99, 100.0, 49.99, 15.0]


exchange_rate = 0.87


prices_eur = [round(price * exchange_rate, 2) for price in prices_usd]

print("Prices in USD:", prices_usd)
print("Prices in EUR:", prices_eur)