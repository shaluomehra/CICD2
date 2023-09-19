# What is a dictionary?

#Uses key/value pairs
#Key is the reference to the object

#Making a Dictionary

student_1 = {"name":"Shaluo",
             "stream":"DevOps",
             "completed_lessons":4,
             "completed_lesson_names":["variables","data types","operators"]}

print(student_1)

#Accessing data using keys

print(student_1["stream"])

#changing a value in a dict

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lesson_names"].remove("data types")
print(student_1)

#Getting the keys

print(student_1.keys())

#Sets & Frozen Sets

car_parts = {"wheels", "doors", "exhaust", "windows"}
print(car_parts) # unordered, cannot be duplicate items

car_parts.add("steering wheel")
print(car_parts)

car_parts.discard("windows")
print(car_parts)

#Frozen Sets, immutable set

x = frozenset([1,2,3,4,5])