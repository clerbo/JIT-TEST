import requests
import pypokedex
import urllib3
import tkinter as tk
from io import BytesIO 
import random

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
  pass

# -- ITEMS -- #
print()
URL = 'https://pokeapi.co/api/v2/item/master-ball/'

print("There are two different types of pokeballs you can use to capture " + str(n) + "!")

while True:
  ball = input("One pokeball is the master ball, and another pokeball is the quick ball. Type one to learn more about it, or type 'next' to continue: ")
  print()
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
      print()
    continue
  
  elif ball == "quick ball":
    URL = 'https://pokeapi.co/api/v2/item/quick-ball/'
    trace("Calling", URL)
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    trace("\nText Returned:", response.text)
    
    item = requests.get(URL)
    data = item.json()
    for effect in data["effect_entries"]:
      print(effect['effect'])
      print()
    continue

  elif ball == "next":
    break
  
  else:
    print("Ooops! Try again.")
    break
  

print()
print("Let's see if you can catch your Pokemon with the ball you chose!")
type = input("Choose which ball you want to use to catch your Pokemon: ")
print()
if type == "master ball":
  list2 = ['Yes', 'No']
  result = random.choice(list2)
  if result == "Yes":
    print("You caught the Pokemon! Congratulations!")
  if result == "No":
    print("Sorry, you didn't catch the Pokemon.")
if type == "quick ball":
  list2 = ['Yes', 'No']
  result = random.choice(list2)
  if result == "Yes":
    print("You caught the Pokemon! Congratulations!")
  if result == "No":
    print("Sorry, you didn't catch the Pokemon.")
print()