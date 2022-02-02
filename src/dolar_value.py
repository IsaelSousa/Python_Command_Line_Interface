import requests
import json

class DolarValue:
  req = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
  price = req.json()

  # Coin Price
  coin = price["USD"]["name"]
  # Coin Data
  date = price["USD"]["create_date"]
  # Current Value
  bid = price["USD"]["bid"]
  # Max value
  maxvalue = price["USD"]["high"]
  # Min value
  minvalue = price["USD"]["low"]