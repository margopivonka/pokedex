# testing/my_test.py
# test pokemon_name function

from app.my_app import pokemon_info, pokemon_image

def test_pokemon_info():
    result = pokemon_info(7)["name"]
    assert result == "Squirtle"

def test_pokemon_image():
    result = pokemon_image(7)
    assert result == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"

