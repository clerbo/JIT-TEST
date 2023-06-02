import requests
import pypokedex
import urllib3
import tkinter as tk
from io import BytesIO 

# -- DESCRIPTION/POKEDEX -- #

n = input("What Pokemon would you like to know more about?")
pokemon = pypokedex.get(name = str(n)) 
print("The Pokedex number for this Pokemon is " + str(pokemon.dex) + ".")
print("These are the types that this Pokemon is: " + str(pokemon.types))
print("This Pokemon weighs " + str(pokemon.weight) + " pounds.")


def trace(*args):
  for debug in output:
    print(*args)
    pass
    
URL = "https://pokeapi.co/api/v2/pokemon/{id or name}/"
trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

trace("\nHere are all the key/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)

# -- ABILITIES -- #
URL = "https://pokeapi.co/api/v2/ability/static"

def trace(*args):
  for debug in output:
    print(*args)
    pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

effect_changes = data["effect_changes"]
for entry in effect_changes:
  print ()
  for item in entry["effect_entries"]:
    if item["language"]["name"] == "en":
      print (item["effect"])

trace("\nHere are all the key/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)
  

# -- ITEMS -- #
URL = "https://pokeapi.co/api/v2/item/master-ball/"

def trace(*args):
  for debug in output:
    print(*args) #comment this line out later to remove debug output
    pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

trace("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)