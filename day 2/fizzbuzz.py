# Get an input from the user


num = int(input("Enter a number: "))

# Check for multiples of 3 and/or 5

#if number is divisible by 3 & 5 print FizzBuzz
#if number is divisible by 3 print Fizz
#if number is divisible by 5 print Buzz
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
     print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Neither Fizz or Buzz")
