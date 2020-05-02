#web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect, request, flash

home_routes = Blueprint("home_routes", __name__)

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

@home_routes.route("/quiz/submit", methods=["GET", "POST"])
def quiz_submit():
    print("SUBMITTED QUIZ RESULTS") #build API using inputs, not sure if we need this tbh
    #  print("FORM DATA:", dict(request.form)) #> {'full_name': 'Example User', 'email_address': 'me@example.com', 'country': 'US'}
     # user = dict(request.form)
    # todo: store in a database or google sheet!
     # flash(f"User '{user['full_name']}' created successfully!", "success")
    #flash(f"User '{user['full_name']}' created successfully! (TODO)", "warning")
    return redirect("/")

@home_routes.route("/animation")
def animation():
    print("VISITED ANIMATION")
    return render_template("animation.html")

