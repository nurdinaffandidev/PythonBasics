
def output_age():
    try:
        age = int(input("Age: "))
        print(f"Input age = {age}")
    except ValueError:
        print("Invalid input")


output_age()
print("-----------------------\n")

def output_risk(age):
    try:
        income = 2000
        risk = income / age
        return round(float(risk),2)
    except ZeroDivisionError:
        print("Age can't be zero")
        return None

input_age = int(input("input age: "))
# print(f"Risk score = {output_risk(input_age):.2f}") #format string float 2 d.p
print(f"Risk score = {output_risk(input_age)}")