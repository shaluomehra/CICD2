#Functions

#DRY - Don't repeat yourself

#Allow us to embed/reference code so that we can re use it multiple times.

#Making a function

def print_something(print_string):
    print(print_string)

print_something("We can pass anything")

def greeting(name):
    print(f"Hello my name is {name}")

greeting("Shaluo")

# The return statement
def addition(int1=0,int2=0):
     return int1 + int2

print(addition())
print(addition(4,5))

#multiple arguments
# use * as a wildcard and this can be as many arguments as you like

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)
    print(type(multiargs))
multi_args(1,2,3,4,5)

#Type Hints

#Function Good Practices

#Add useful comments to explain your functions
#Clear function names and argument names
#Keep your functions small and compact
#Avoid Duplication
#Put functions at the start of your code
#Remember Return
#Do One Thing

