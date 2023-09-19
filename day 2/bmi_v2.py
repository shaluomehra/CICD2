name = input("What is your name? ")
Weight = input("What is your weight in kilograms ? ")
Height = input("What is your height in metres ? ")

height_sq = float(Height)**2

bmi = float(Weight)/height_sq

# under 18.5 – This is described as underweight.
# between 18.5 and 24.9 – This is described as the 'healthy range'.
# between 25 and 29.9 – This is described as overweight.
# between 30 and 39.9 – This is described as obesity.
# 40 or over – This is described as severe obesity.

print(f"{name} your BMI is: {bmi:.1f}")
if bmi < 18.5:
    print("You are under weight")
elif 18.5 <= bmi <= 24.9:
    print("You are a healthy weight")
elif 25 <= bmi <= 29.9:
    print("You are over weight")
elif 30 <= bmi <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")

