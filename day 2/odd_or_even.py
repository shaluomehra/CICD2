#Create a check to see if a number that is inputted is odd or even

#First create an input

number = int(input("Enter a number: "))
#if the number has a remainder of 0 when dividing by 2 then it is even
if number % 2 == 0:
    print("Even number")
#otherwise it is odd
else:
    print("Odd Number")
