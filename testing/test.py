#test pokemon_name function

from app.get_api import pokemon_info

def test_pokemon_info():
    result = pokemon_info(7)["name"]
    assert result == "Squirtle"
