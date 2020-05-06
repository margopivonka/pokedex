## combining quiz and api functionality for one file
#packages/modules to import
import os
import json
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def pokemon_info(number):
    request_url = f"http://pokeapi.co/api/v2/pokemon/{user_score}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def pokemon_image(number):
    request_url2 = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{user_score}.png"
    return request_url2

# Favorite color
def get_score():
    
    if results["choice1"]=="red":
        color_value=1
    if results["choice1"]=="blue":
        color_value=2
    if results["choice1"]=="green":
        color_value=3
    if results["choice1"]=="yellow":
        color_value=4
    #print(color_value)
    
    if results["choice2"]=="fall":
        season_value=1
    if results["choice2"]=="winter":
        season_value=2
    if results["choice2"]=="spring":
        season_value=3
    if results["choice2"]=="summer":
        season_value=4
    #print(season_value)

    if results["choice3"]=="pizza":
        food_value=1
    if results["choice3"]=="tacos":
        food_value=2
    if results["choice3"]=="noodles":
        food_value=3
    if results["choice3"]=="nugs":
        food_value=4
    #print(food_value)

    if results["choice4"]=="dog":
        animal_value=1
    if results["choice4"]=="cat":
        animal_value=2
    if results["choice4"]=="monkey":
        animal_value=3
    if results["choice4"]=="tiger":
        animal_value=4
    #print(animal_value)

    if results["choice5"]=="earth":
        element_value=1
    if results["choice5"]=="wind":
        element_value=2
    if results["choice5"]=="fire":
        element_value=3
    if results["choice5"]=="water":
        element_value=4
    #print(element_value)

    user_score=color_value+season_value+food_value+animal_value+element_value
    print("SCORE: ", user_score)
data = pokemon_info(user_score)
name = data["name"].title()

image_data = pokemon_image(user_score)
img = mpimg.imread(image_data)
plt.imshow(img)
plt.show()

print(name)

breakpoint()