# What is a Boolean

#Binary option between True or False

a = True
b = False

print(a == b)
print (a != b)
print (a >= b) # True 1 > 0

print (True and False) # False#

#Boolean Methods

hi = "Hello World"
print(hi.isalnum()) # False (only alphabetca chars)
print(hi.endswith("d")) # True

#Boolean Values
x = 0
y = "hello"

print(bool(x)) # False
print(bool(y)) # True

#Value of None
#Use as placeholder

z = None

print(bool(z)) # False
print(z == False) # Also False
print(z is None) # True

print(type(z))
