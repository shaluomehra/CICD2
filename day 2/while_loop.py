#While Loops

#For loops are all to do with iterating through collections

# While loops are more like a monitor -> while something is true then do something

x = 0

while x < 10:
    print(f"It's working --> {x}")
    if x == 4:
        break
    x += 1

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 120:
        user_prompt = False
    else:
        print("Invalid age")

print(f"Your age is {age}")