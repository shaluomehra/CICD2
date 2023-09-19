#what are operators

#symbols that execute a particular mathematical or logical function

#numeric types

#integers, floats, complex
a = 1
b = 0.2
c = 0.3

print(a + b)

#strings

hw = "Hello World!"

print(hw[6:])
print(hw[:5])
print(hw[-1])

#String Methods

strip_string = "Hi my name is Shaluo           "
print(len(strip_string))
# removes the white space
print(len(strip_string.strip()))

example_text = "Here's some text with lots of text"
print(example_text.count("text"))
# since the word text comes up twice
print(example_text.lower())
#lower case

print(example_text.replace("with",","))

#Casting

a = 1
b = 2.5
c = "3"

print(a + b + int(c))

#Concatenation

d = "Theres now a number 12.5 unless theres a space"

#F-Strings

name = "Shaluo"
years = 7
height = 60.2

print(f"{name} is {years} years old and is {height}cm tall")

Snoop = "Snoopy"
snoop_years = 52

print(f"{Snoop.upper()} IS {snoop_years * 7} YEARS OLD IN DOG YEARS")