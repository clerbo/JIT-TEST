import requests
"""
# -- DESCRIPTION/POKEDEX -- #
URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

def trace(*args):
  #for debug output
  print(*args)
  pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

trace("\nHere are all the key/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)
"""
# -- ABILITIES -- #
URL = "https://pokeapi.co/api/v2/ability/static"

def trace(*args):
  #for debug output
  print(*args)
  pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

print (data["effect_changes"])
effect_changes = data["effect_changes"]
for entry in effect_changes:
  print ()
  print (entry["effect_entries"])
  for item in entry["effect_entries"]:
    if item["language"]["name"] == "en":
      print (item["effect"])

#def name(params):
  #URL = f'https://pokeapi.co/api/v2/ability?q={name}'
  #response = requests.get(URL)
  #

trace("\nHere are all the key/value pairs in the JSON response:")
#for key, value in data.items():
#  trace (key, ": ", value)
  
"""
# -- ITEMS -- #
URL = "https://pokeapi.co/api/v2/item/master-ball/"

def trace(*args):
  #for debug output
  #print(*args) #comment this line out later to remove debug output
  pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

trace("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)
"""