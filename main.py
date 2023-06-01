import requests

# -- ABILITIES -- #
URL = "https://pokeapi.co/api/v2/ability/"

response = requests.get(URL)
response.raise_for_students()



# -- ITEMS -- #
url:"https://pokeapi.co/api/v2/item"