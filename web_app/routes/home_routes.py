#web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect, request, flash
from random import randint
home_routes = Blueprint("home_routes", __name__)

#
# Set up page routes
#
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
    scale = randint(1,40)
    user_score = user_score * scale

    print("SCORE: ", user_score)

    flash("Quiz submitted successfully!", "success")

    return redirect("/")
    #add redirect to take them to a page with poke icon


 



@home_routes.route("/animation")
def animation():
    print("VISITED ANIMATION")
    return render_template("animation.html")

