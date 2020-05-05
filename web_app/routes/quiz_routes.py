from flask import Blueprint, render_template, request

from app.get_api import pokemon_info

quiz_routes = Blueprint("quiz_routes", __name__)

#@quiz_routes.route("/results", methods=["GET", "POST"])
#def results(choice=None):
#    print("VISITING THE RESULTS PAGE")
#    print("REQUEST PARAMS:", dict(request.args))
#    print("REQUEST VALUES:", dict(request.values))
#
#    options = ["rock", "paper", "scissors"]
