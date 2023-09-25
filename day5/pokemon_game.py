import json
import requests

def get_pokemon():
    pokemon = str(input("Enter a pokemon ").lower())
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    return json.loads(response.text)

# Function to simulate a battle between two Pokémon
def battle(player_pokemon, player2_pokemon):
    player_attack = player_pokemon["stats"][1]["base_stat"]
    player2_attack = player2_pokemon["stats"][1]["base_stat"]

    if player_attack > player2_attack:
        return "Player 1 wins!"
    elif player_attack < player2_attack:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

player_pokemon = get_pokemon()
player2_pokemon = get_pokemon()

print(f"Player 1 chose {player_pokemon['name']}!")

# Simulate the battle
result = battle(player_pokemon, player2_pokemon)

print(f"Player 2 chose {player2_pokemon['name']}!")
print(f"The battle result is: {result}")

