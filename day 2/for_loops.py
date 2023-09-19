#For Loops

#Python uses 'for' only, no 'for each' loops

list_data=[1,2,3,4,5]
embedded_list = [[1,2,3],[4,5,6]]
dict_data = {
    1: {"name":"Bronson",
        "money":"£0.05"},
    2: {"name":"Masha",
        "money":"£3.66"},
    3: {"name":"Roscoe",
        "money":"£1.14"}
}

print(dict_data)

for num in list_data:
    print(num * 2)

# Nested For Loops

for data in embedded_list:
    print(data)
    for num in data:
        print(num)

#Looping through dictionaries

# for item in dict_data.values():
#     for embed in item.values():
#         print(embed)

for items in dict_data.values():
    print(items["money"])

#loops and if statements

for num in list_data:
    if num == 3:
        print("I found 3")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too Soon!")