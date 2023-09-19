#Collections can store multiple pieces of data inside

#Lists

shopping_list = ["Salad", "Eggs", "Donuts", "Milk", "Salmon"]

print(shopping_list)
print(type(shopping_list))
print(shopping_list[0])

shopping_list[2] = ("Tomato")
print(shopping_list)

#List Methods

#Add something to the list
shopping_list.append("Carrots") #adds on to the list
shopping_list.extend(["Water", "Celery"]) # adds on multiple items on a list
print(shopping_list)

shopping_list.pop() #pops out the last item on the list can be used with indexes too
print(shopping_list)

shopping_list.remove("Salad") # removes all instances of salad in my list
print(shopping_list)

#Mixed Data Type Lists

mixture = [1,2,3.5,"hello"]
print(mixture)

#List Slicing
print(mixture[1:3]) # prints index 1 and 2 but not 3
print(mixture[::-1]) # reverses the list

#Tuples

essentials = (1,2,3,"bread","eggs")
print(essentials)
print(type(essentials))
