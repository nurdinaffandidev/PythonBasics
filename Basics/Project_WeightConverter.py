'''
Exercise:
    User enter weight
    User enter unit lbs or kg
    Print weight and unit
'''

weight = float(input("Enter weight: "))
unit = input("Enter unit: (L)bs or (K)g: ")
if unit.upper() == "L":
    weight = weight * 0.45
    print(f"Your weight is {weight} lbs")
elif unit.upper() == "K":
    print(f"Your weight is {weight} kg")
else:
    print("You have entered invalid input(s)")