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

