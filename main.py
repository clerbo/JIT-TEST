import requests
import pypokedex
import urllib3
import tkinter as tk
from io import BytesIO 

# -- DESCRIPTION/POKEDEX -- #

n = input("What Pokemon would you like to know more about? ")
pokemon = pypokedex.get(name = str(n)) 
print("The Pokedex number for this Pokemon is " + str(pokemon.dex) + ".")
print("These are the types that this Pokemon is: " + str(pokemon.types))
print("This Pokemon weighs " + str(pokemon.weight) + " pounds.")


def trace(*args):
  for debug in output:
    print(*args)
    pass
print()

# -- ABILITIES -- #
def trace(*args):
  for debug in output:
    print(*args)
    pass

print("These are the abilities the Pokemon has: " + str(pokemon.abilities))

"""
URL = 'https://pokeapi.co/api/v2/ability/'
for ability in abilities:
  print (item['name'])

import http.client

conn = http.client.HTTPConnection("pokeapi.co")

payload = "{}"

conn.request("GET", "/api/v2/ability/%7Bparam1%7D/", payload)

res = conn.getresponse()
data = res.read()
      
print(data.decode("utf-8"))


trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

effect_changes = data["effect_changes"]
ability = effect_changes.get(name = str(ability))
for entry in effect_changes:
  print ()
  for item in entry["effect_entries"]:
    if item["language"]["name"] == "en":
      print (item["effect"])
"""
