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
    print(results)
    print(results["choice1"])

    if results["choice1"]=="red":
        print("user_score=1")
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

