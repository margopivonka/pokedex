#Importing Pokemon API KEY

# source: https://github.com/RaspberryPiFoundation/python-curriculum/blob/master/en-GB/lessons/Pokedex/Project%20Resources/pokeapi.py

import os
import json
import requests
from dotenv import load_dotenv



def get_pokemon_name(number):
    request_url = f"http://pokeapi.co/api/v1/pokemon/{num}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    #pokemonDict = json.loads(data.decode("UTF-8"))
    return parsed_response #pokemonDict


num = str(input("Select a number between 1 and 151: "))

data = get_pokemon_name(num)


print(data["name"].title())

# dictionary keys
# (['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'species', 'sprites', 'stats', 'types', 'weight'])
# (get_pokemon_name(num))["name"] worked in breakpoint to get name

