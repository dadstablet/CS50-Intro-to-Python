import requests
import sys

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

try:
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=aa6e170cd0321a44cc4ce8d7c81ad3d6388399c67a829f3cf4e678ea97675e37")
    content = r.json()
    price = float(content["data"]["priceUsd"])
    user_price = n * price
    print(f"${user_price:,.4f}")
except requests.RequestException:
    pass

