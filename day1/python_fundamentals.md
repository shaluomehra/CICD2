# Day 1 Markdown

## Hello World
Using print and quotations you can print a line of code on the screen <br>
`print("Hello World!)`

Using the input() function you can get an input from the user and assign it a value using a variable name<br>
`name = input("What is your name ? ")`


## Data Types
### Numeric Types
There are 3 numeric data types
- Integer
- Float
- Complex

Using +, -, /, *, %, we can perform functions on our numeric types

### Strings
A word or multiple words in quotation marks would be a string

`hw = "hello world!"`

String slicing can be used to get a certain part of a string
```python
print(hw[0]) #Will print h
print(hw[6:]) #Will print world!
print(hw[:5]) #Will print hello
print(hw[-1]) #Will print !
```

You can also use some string methods that will perform a function on the string like .strip()
```python
strip_string = "Hi my name is Shaluo           "
print(len(strip_string)) # prints 31
# removes the white space
print(len(strip_string.strip()))
#prints 20
```
and .count()
```python
example_text = "Here's some text with lots of text"
print(example_text.count("text"))
```
Will print 2 since the word text comes up twice

## F-Strings in Python

F-strings, also known as formatted string literals, provide a concise and powerful way to embed expressions inside string literals in Python.

### Syntax

The basic syntax of an f-string is as follows:

```python
name = "Alice"
age = 30

# Creating an f-string
greeting = f"Hello, my name is {name} and I am {age} years old."

# Output: "Hello, my name is Alice and I am 30 years old."
```
### Formatting with F-Strings
You can also apply formatting to the expressions within f-strings by using the usual formatting specifiers. For example:

```python
pi = 3.141592653

# Formatting pi to 2 decimal places
formatted_pi = f"The value of pi is approximately {pi:.2f}."

# Output: 'The value of pi is approximately 3.14.'
```
### Booleans

Booleans are a binary option between true and false

```
a = True
b = False
print(a == b)
print (a != b)
print (a >= b) # True 1 > 0
```
First line would print False <br>
Second line would print True <br>
Third line would print True <br>

These are useful and can be used with comparison operators

## Collections

### Lists
Using collections can be useful when a variable needs to have multiple values <br>
You can create  list by using square brackets <br>

`shopping_list = ["Salad", "Eggs", "Donuts", "Milk", "Salmon"]`

Lists use indexing and can be called, changed and sliced
```python
shopping_list[2] = ("Tomato")
print(shopping_list)
```
This line of code would change the third item on the list to 'Tomato' 

### Tuples

Tuples are immutable meaning they cannot be changed or reassigned

We create a tuple using parenthesis ()

### Dictionaries

Dictionaries are mutable data structures that allow you to store key-value pairs
```python
student_1 = {"name":"Shaluo",
             "stream":"DevOps",
             "completed_lessons":3,
             "completed_lesson_names":["variables","data types","operators"]}
```
We can call a value from the dictionary using it's key

`print(student_1["stream"])`

Would print 'DevOps'