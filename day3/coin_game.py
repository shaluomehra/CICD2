#Import the random module
import random
#create a list of possible results from a coin flip
coin = ["Heads","Tails"]
# using random.choice() we can randomise the result of the variable we place in the parenthesis
result = random.choice(coin)
print(result)
