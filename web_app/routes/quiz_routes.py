from flask import Blueprint, render_template, request

from app.get_api import pokemon_info

quiz_routes = Blueprint("quiz_routes", __name__)

