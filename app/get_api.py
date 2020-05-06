#Importing Pokemon API KEY

# source: https://github.com/RaspberryPiFoundation/python-curriculum/blob/master/en-GB/lessons/Pokedex/Project%20Resources/pokeapi.py

import os
import json
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def pokemon_info(number):
    request_url = f"http://pokeapi.co/api/v2/pokemon/{num}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    #pokemonDict = json.loads(data.decode("UTF-8"))
    return parsed_response #pokemonDict

def pokemon_image(number):
    request_url2 = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{num}.png"
    #response2 = requests.get(request_url2)
    #parsed_response = json.loads(response2.text)
    return request_url2


num = str(input("Select a number between 1 and 807: "))

data = pokemon_info(num)
name = data["name"].title()

image_data = pokemon_image(num)
img = mpimg.imread(image_data)
plt.imshow(img)
plt.show()

print("You are a total",name, "!")




# dictionary keys
# (['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'species', 'sprites', 'stats', 'types', 'weight'])
# (get_pokemon_name(num))["name"] worked in breakpoint to get name


# data["sprites"]["front_default"]
# https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png


#this are the types of keys available for sprites, sprites are images of the pokemon
#data["sprites"].keys()
#dict_keys(['back_default', 'back_female', 'back_shiny', 'back_shiny_female', 'front_default', 'front_female', 'front_shiny', 'front_shiny_female'])
