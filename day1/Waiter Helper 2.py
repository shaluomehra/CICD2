#List all the starters, mains, desserts, drinks

Starters = ["Soup","Garlic Bread","Salad"]
Mains = ["Chef's Pasta","Chicken Curry","Mozzarella Pizza"]
Desserts = ["Ice Cream","Chocolate Cake"]
Drinks = ["Coke","Fanta","Still Water"]


#get starter input
print(Starters)
user_starter = input("Hi and welcome to Shaluo's restaurant, what can I start you up with? ")
#if statement to make sure they input a valid selection
if user_starter in Starters:
      print("Great Choice!")
else:
      print("Invalid Choice")
#get mains input
print(Mains)
user_mains = input("What would you like for the main course? ")
#if statement to make sure they input a valid selection
if user_mains in Mains:
      print("Great Choice!")
else:
      print("Invalid Choice")
#get desserts input
print(Desserts)
user_desserts = input("What would you like for dessert?  ")
if user_desserts in Desserts:
      print("Great Choice!")
else:
      print("Invalid Choice")
#get drinks input
print(Drinks)
user_drinks = input("Finally what would you like to drink?  ")
if user_drinks in Drinks:
      print("Great Choice!")
else:
      print("Invalid Choice")
#print out the users choices
print(f"Brilliant! So that would be {user_starter} to start with \n"
      f"And {user_mains} as your main course \n"
      f"For Dessert you'll be having {user_desserts} \n"
      f"Finally to drink you'll have {user_drinks}")




