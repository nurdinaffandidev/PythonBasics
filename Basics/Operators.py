# Logical operators
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
elif has_high_income and not has_good_credit:
    print("Work on credit")
elif has_good_credit and not has_high_income:
    print("Work on income")
else:
    print("No eligible for loan")

# Comparison operators
temperature = 21
if temperature > 30:
    print("It's a hot day")
elif temperature > 20 and temperature <= 30:
    print("It's a fine day")
elif temperature <= 20:
    print("It's a cold day")