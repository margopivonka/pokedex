# app/my_app.py

#packages/modules to import
import os
import json
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import randint
load_dotenv()
import requests

def pokemon_info(number):
    request_url = f"http://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def pokemon_image(number):
    request_url2 = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
    return request_url2

if __name__ == "__main__":

    valid_options = ["A", "B", "C", "D"]

    # FAVORITE COLOR
    color = input("What is your favorite color? \n A. Red \n B. Blue \n C. Green \n D. Yellow \n \n Please enter corresponding letter: ").upper()
    
    if color in valid_options:
        pass
    else:
        print("Please choose either A, B, C, or D")
        quit()

    if color =="A":
        color_value = 1
    elif color == "B":
        color_value = 2
    elif color == "C":
        color_value = 3
    elif color == "D":
        color_value = 4

    # FAVORITE SEASON
    season = input("What is your favorite season? \n A. Fall \n B. Winter \n C. Spring \n D. Summer \n \n Please enter corresponding letter: ").upper()
    
    if season in valid_options:
        pass
    else:
        print("Please choose either A, B, C, or D")
        quit()

    if season =="A":
        season_value = 1
    elif season == "B":
        season_value = 2
    elif season == "C":
        season_value = 3
    elif season == "D":
        season_value = 4

    # FAVORITE FOOD
    food = input("What is your favorite food? \n A. Pizza \n B. Tacos \n C. Noodles \n D. Burgers \n \n Please enter corresponding letter: ").upper()
    
    if food in valid_options:
        pass
    else:
        print("Please choose either A, B, C, or D")
        quit()

    if food =="A":
        food_value = 1
    elif food == "B":
        food_value = 2
    elif food == "C":
        food_value = 3
    elif food == "D":
        food_value = 4

    # FAVORITE ANIMAL
    animal = input("What is your favorite animal? \n A. Dog \n B. Cat \n C. Monkey \n D. Tiger \n \n Please enter corresponding letter: ").upper()
    
    if animal in valid_options:
        pass
    else:
        print("Please choose either A, B, C, or D")
        quit()

    if animal =="A":
        animal_value = 1
    elif animal == "B":
        animal_value = 2
    elif animal == "C":
        animal_value = 3
    elif animal == "D":
        animal_value = 4

    # ELEMENTAL ID
    element = input("What earthly element do you best identify with? \n A. Earth \n B. Wind \n C. Fire \n D. Water \n \n Please enter corresponding letter: ").upper()
    
    if element in valid_options:
        pass
    else:
        print("Please choose either A, B, C, or D")
        quit()

    if element =="A":
        element_value = 1
    elif element == "B":
        element_value = 2
    elif element == "C":
        element_value = 3
    elif element == "D":
        element_value = 4
    else:
        element = input("Please enter either a, b, c, or d.")

    user_score=color_value+season_value+food_value+animal_value+element_value
    user_score = user_score * randint(1,40)

    #FIND POKEMON NAME
    data = pokemon_info(user_score)
    name = data["name"].title()

    #FIND POKEMON IMAGE
    image_data = pokemon_image(user_score)
    img = mpimg.imread(image_data)

    #PRINT SCORE, NAME, IMAGE
    print("SCORE: ", user_score)
    print(f"You are a {name}! This means that you are totally awesome!!!")
    plt.imshow(img)
    plt.show()
