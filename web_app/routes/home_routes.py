#web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect, request, flash

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
    #print("FORM DATA:", dict(request.form)) #> {'full_name': 'Example User', 'email_address': 'me@example.com', 'country': 'US'}
    #print("REQUEST VALUES:", dict(request.values))
    results=dict(request.form) #turns user results into a dictionary so we can assign and add up the values
    #print(results)
    #print(results["choice1"])

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



    #
    # should be able to use if statements to assign and add up values
    #
    #user = dict(request.form)
    # todo: store in a database or google sheet!
     # flash(f"User '{user['full_name']}' created successfully!", "success")
    #flash(f"User '{user['full_name']}' created successfully! (TODO)", "warning")
    return redirect("/")
    #add redirect to take them to a page with poke icon


    #def results(choice=None):
    #print("VISITING THE RESULTS PAGE")
    #print("REQUEST PARAMS:", dict(request.args))
    #print("REQUEST VALUES:", dict(request.values))

    options = ["rock", "paper", "scissors"]

@home_routes.route("/animation")
def animation():
    print("VISITED ANIMATION")
    return render_template("animation.html")

