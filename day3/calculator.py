#Basic Calculator

#Create addition, multiplication, division, subtraction functions

def add(x,y):
    return x + y
def minus(x,y):
    return x - y
def multiply(x,y):
    return x * y
def div(x,y):
    return(x/y)

#Ask the user for an input

choice = int(input("Please select which operation you'd like to do\n"
                   "1. Addition \n"
                   "2. Subtraction \n"
                   "3. Multiplication \n"
                   "4. Division \n"))

#Ask the user which numbers they'd like to operate on

num1 = float(input("Enter your first number "))
num2 = float(input("Enter your second number "))

#If Statements depending on what the user has selected
if choice == 1:
    print(f"{num1} + {num2} is equal to: ")
    print(add(num1,num2))

elif choice == 2:
    print(f"{num1} - {num2} is equal to: ")
    print(minus(num1,num2))

elif choice == 3:
    print(f"{num1} * {num2} is equal to: ")
    print(multiply(num1,num2))
elif choice == 4:
    print(f"{num1} + {num2} is equal to: ")
    print(div(num1,num2))
#if the user enters a wrong input tell them that they have
else:
    print("Invalid Input")


