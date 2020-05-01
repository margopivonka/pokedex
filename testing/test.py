#test pokemon_name function

from app.get_api import pokemon_name

def test_pokemon_name():
    result = pokemon_name(7)
    assert result == "Squirtle"
