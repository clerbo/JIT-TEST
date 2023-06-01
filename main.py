import requests
import pypokedex
import urllib3
import tkinter as tk
import PIL.image
from io import BytesIO 

# -- DESCRIPTION/POKEDEX -- #

name = input("What Pokemon would you like to know more about?")
pokemon = pypokedex.get(name) 
print(pokemon.dex)
print(pokemon.name)
print(pokemon.types)

def trace(*args):
  for debug output
  print(*args)
  pass

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
  for debug output
  print(*args)
  pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

trace("\nHere are all the key/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)
  

# -- ITEMS -- #
URL = "https://pokeapi.co/api/v2/item/master-ball/"

def trace(*args):
  for debug output
  print(*args) #comment this line out later to remove debug output
  pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

trace("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)