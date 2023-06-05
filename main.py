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

print()

# -- ABILITIES -- #
print("These are the abilities the Pokemon has: " + str(pokemon.abilities))

def trace(*args):
  #print(*args)
  pass

# -- ITEMS -- #
print()
URL = 'https://pokeapi.co/api/v2/item/master-ball/'

print("There are two different types of pokeballs you can use to capture " + str(n) + "!")
ball = input("One pokeball is the master ball, and another pokeball is the ___. Type one to learn more about them: ")

if ball == "master ball":
  trace("Calling", URL)
  response = requests.get(URL)
  response.raise_for_status()
  data = response.json()
  trace("\nText Returned:", response.text)

  item = requests.get(URL)
  data = item.json()
  for effect in data["effect_entries"]:
    print(effect['effect'])

