#Control Flow - control the flow of the code

#Check if conditions are true before you run a piece of code

#if, elif, else

#if
age = 18

if age >= 18:
    print("You are old enough to watch this movie")
if age < 18:
    print("Sorry, you are not old enough to watch this movie")

# elif less processing power, only runs when the if statement is not met

film_rating = ("12a")

if film_rating.lower() == "u":
    print("All age groups can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidance is advised for this movie")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("People aged 12 or over can watch this film unsupervised. Younger people must be supervised")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie")
elif film_rating.lower() == "18":
    print("People aged 18 can watch this movie")

#else
else:
    print("This is not a valid rating")

#In python there are no Switch statements or case statements