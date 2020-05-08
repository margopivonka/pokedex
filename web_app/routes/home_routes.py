#web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect, request, flash
from random import randint

home_routes = Blueprint("home_routes", __name__)

import os
import json
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Set up page routes
@home_routes.route("/")
def home_page():
    print("VISITED HOME PAGE")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED ABOUT PAGE")
    return render_template("about.html")

@home_routes.route("/quiz")
def quiz():
    print("VISTED QUIZ PAGE")
    return render_template("quiz.html")

@home_routes.route("/results", methods=["GET", "POST"])
def quiz_submit(choice=None):
    print("SUBMITTED QUIZ RESULTS") #build API using inputs, not sure if we need this tbh
    
    results=dict(request.form) #turns user results into a dictionary so we can assign and add up the values

    def pokemon_info(number):
        request_url = f"http://pokeapi.co/api/v2/pokemon/{number}"
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)
        return parsed_response

    def pokemon_image(number):
        request_url2 = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
        return request_url2

    if results["choice1"]=="red":
        color_value=1
    if results["choice1"]=="blue":
        color_value=2
    if results["choice1"]=="green":
        color_value=3
    if results["choice1"]=="yellow":
        color_value=4
    
    if results["choice2"]=="fall":
        season_value=1
    if results["choice2"]=="winter":
        season_value=2
    if results["choice2"]=="spring":
        season_value=3
    if results["choice2"]=="summer":
        season_value=4

    if results["choice3"]=="pizza":
        food_value=1
    if results["choice3"]=="tacos":
        food_value=2
    if results["choice3"]=="noodles":
        food_value=3
    if results["choice3"]=="nugs":
        food_value=4

    if results["choice4"]=="dog":
        animal_value=1
    if results["choice4"]=="cat":
        animal_value=2
    if results["choice4"]=="monkey":
        animal_value=3
    if results["choice4"]=="tiger":
        animal_value=4

    if results["choice5"]=="earth":
        element_value=1
    if results["choice5"]=="wind":
        element_value=2
    if results["choice5"]=="fire":
        element_value=3
    if results["choice5"]=="water":
        element_value=4

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
    print(f"You are a {name}! This means you are totally awesome!!!")
    
    flash("Quiz submitted successfully!", "success")

    return render_template("results.html",
        user_score=user_score,
        img = img,
        name=name
    )
    #add redirect to take them to a page with poke icon

@home_routes.route("/pokemon")
def quiz_results():
    print("VISITED RESULTS PAGE")
    return render_template("results.html")


@home_routes.route("/animation")
def animation():
    print("VISITED ANIMATION")
    return render_template("animation.html")

