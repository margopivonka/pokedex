#practice_app.py in root directory

from flask import Flask

app = Flask(__name__)

import os
import json
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


@app.route("/")
def hello_world():
    return "Hello, World"

# 
# 
# def pokemon_info(number):
#     request_url = f"http://pokeapi.co/api/v2/pokemon/{num}"
#     response = requests.get(request_url)
#     parsed_response = json.loads(response.text)
#     #pokemonDict = json.loads(data.decode("UTF-8"))
#     return parsed_response #pokemonDict
# 
# def pokemon_image(number):
    request_url2 = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{num}.png"
    #response2 = requests.get(request_url2)
    #parsed_response = json.loads(response2.text)
    return request_url2
# 
# 
# num = str(input("Select a number between 1 and 807: "))
# 
# data = pokemon_info(num)
# name = data["name"].title()
# 
# image_data = pokemon_image(num)
# img = mpimg.imread(image_data)
# plt.imshow(img)
# plt.show()
# 
# print(name)