#Make some Characters
#Import necessary modules
import random

characters = ["Jon Snow", "Ned Stark", "Arya Stark",
              "Brienne of Tarth", "Samwell Tarly", "Tyrion Lannister", "Jaime Lannister"]

#Player 1 chooses a character first
player1 = int(input("Player 1 please choose your character:\n"
              "1. Jon Snow\n"
              "2. Ned Stark\n"
              "3. Arya Stark\n"
              "4. Brienne of Tart\n"
              "5. Samwell Tarly\n"
              "6. Tyrion Lannister\n"
              "7. Jaime Lannister\n"
              "Enter any other number for a random character\n"))

# Using indexing, match the input from the player with the list of characters

if 1 <= player1 <= 7:
    choice = characters[player1 - 1]
else:
    #If the user enters a number not inbetween 1 and 7 then it will choose a character at random
    print("Choosing randomly.")
    choice = random.choice(characters)

#Player 2 chooses a character next

player2 = int(input("Player 1 please choose your character:\n"
              "1. Jon Snow\n"
              "2. Ned Stark\n"
              "3. Arya Stark\n"
              "4. Brienne of Tarth\n"
              "5. Samwell Tarly\n"
              "6. Tyrion Lannister\n"
              "7. Jaime Lannister\n"
              "Enter any other number for a random character\n"))

if 1 <= player2 <= 7:
    #dont forget to change the variable name
    choice2 = characters[player2 - 1]
else:
    print("Choosing randomly.")
    choice2 = random.choice(characters)

#print the selected characters
print(choice)
print("versus")
print(choice2)
#Assign some power values to each character
#I've used dictionaries because I can't think of a better way to do this right now.

character_strengths = {
    "Jon Snow": 10,
    "Ned Stark": 6,
    "Arya Stark": 9,
    "Brienne of Tarth": 8,
    "Samwell Tarly": 2,
    "Tyrion Lannister":4,
    "Jaime Lannister":7
}

#struggle to figure this out and then after googling find .get() function hallelujah
'''
get() method in Python is used to get the value of any specified key from a dictionary.
The get() method returns the value of the key if the key is present in the dictionary.
'''

strength_player1 = character_strengths.get(choice)
strength_player2 = character_strengths.get(choice2)

if strength_player1 > strength_player2:
    winner = player1
    print("Winner is player 1")
elif strength_player2 > strength_player1:
    winner = player2
    print("Winner is player 2")
else:
    print("No one (It's a draw)")
