from datetime import datetime

birth_year = input("Birth year: ")
print("birth_year type = ",type(birth_year))
age = datetime.now().year - int(birth_year)
print("age type =  ",type(age))
print("Your age is: " + str(age))

# Exercise:
# Ask a user their weight (in pounds), convert it to kilograms and print on terminal.
print("\nExercise:")
weight_lbs = input("Enter your weight in lbs: ")
weight_kg = float(weight_lbs) * 0.45
print("Your weight is: " + str(weight_kg) + "kg")