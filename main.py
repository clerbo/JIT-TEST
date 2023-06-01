import requests

# -- ABILITIES -- #
URL = "https://pokeapi.co/api/v2/ability/"

def trace(*args):
  #for debug output
  print(*args) #comment this line out later to remove debug output
  pass

trace("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

<<<<<<< HEAD
trace("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)
=======
>>>>>>> 635f098f8854eec510b923a72dcb5616a448d40c
