#Make some Characters

import random

characters = ["Warrior", "Mage", "Rogue", "Knight", "Archer", "Sorcerer", "Assassin"]

print("Welcome to the Simple CLI Fighting Game!\n")

# Player 1 chooses a character
print("Player 1, choose your character (enter a number from 3 to 7):")
print("3. Rogue\n4. Knight\n5. Archer\n6. Sorcerer\n7. Assassin")
choice = int(input())

if 3 <= choice <= 7:
    player1 = characters[choice - 1]
else:
    print("Invalid choice. Choosing randomly.")
    player1 = random.choice(characters[2:])

# Player 2 or CPU chooses a character
if input("Do you have a Player 2? (yes/no): ").lower() == 'yes':
    print("Player 2, choose your character (enter a number from 3 to 7):")
    print("3. Rogue\n4. Knight\n5. Archer\n6. Sorcerer\n7. Assassin")
    choice = int(input())

    if 3 <= choice <= 7:
        player2 = characters[choice - 1]
    else:
        print("Invalid choice. Choosing randomly.")
        player2 = random.choice(characters[2:])
else:
    player2 = random.choice(characters[2:])

# Battle
print(f"\n{player1} vs {player2}!\n")

# Calculate strength values (arbitrary values)
strength_values = {
    "Rogue": 10,
    "Knight": 12,
    "Archer": 9,
    "Sorcerer": 8,
    "Assassin": 11
}

strength_player1 = strength_values.get(player1, 5)  # Default value is 5 for unknown characters
strength_player2 = strength_values.get(player2, 5)

if strength_player1 > strength_player2:
    winner = player1
elif strength_player2 > strength_player1:
    winner = player2
else:
    winner = "No one (It's a draw)"

print(f"The winner is: {winner}!")