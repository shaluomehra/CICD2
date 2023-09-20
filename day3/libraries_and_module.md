# Libraries and Modules in Python

## Introduction

Python has very extensive libraries and modules, this is great for DevOps engineers!

## Modules

SINGLE file of functions, classes, variables etc. That you can bring in and use in another python file


## Libraries

A **library** is a collection of modules. It is a packaged set of pre-written code that can be used to perform common tasks. Needs to be installed with pip.

## Differences

- **Module**: A single Python file that contains reusable code.
- **Library**: A collection of modules that serve related purposes.

## Why They Are Useful

- Code Reusability 
  - Libraries and modules promote code reuse.
  

- Collaboration and Code Sharing 
  - Libraries allow developers to share code with others.


- Common Practices
  - Python's standard library provides a set of modules for performing common tasks.

## Library Example: math
The `math` library is part of Python's standard library and provides a wide range of mathematical functions.

```python
import math

result = math.sqrt(25)
print(result)  # Output: 5.0

```

## Module Example: random
The random module is another part of Python's standard library. It provides functions for generating random numbers.
```python
import random

random_number = random.randint(1, 10)
print(random_number)  # Output: A random integer between 1 and 10 (inclusive)

```