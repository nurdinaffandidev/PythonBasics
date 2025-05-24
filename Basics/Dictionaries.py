"""
name: John Smith
email: johnSmith@gmail.com
age: 30
"""
# init dict
customer = {
    "name" : "John Smith",
    "email": "johnSmith@gmail.com",
    "age" : 30,
    "is_verified" : True,
    12 : 34
}

# get values from key
print(customer["name"])
print(customer[12])
# print(customer["birth_date"]) # KeyError: 'birth_date'
# print(customer["Name"]) # KeyError: 'Name'

print(customer.get("name"))
print(customer.get("Name"))
print(customer.get("birth_date", "Jan 1 1980")) # 2nd param: default value
print(customer)

# amend value of key
customer["name"] = "Jack Doe"
print(customer["name"])

# add new key value
customer["birth_date"] = "Jan 1 1980"
print(customer)

# Exercise: Print out input int value to literal word
phone = input("Enter a number: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}

output_string = ""
for char in phone:
    output_string += digits_mapping.get(char, "!") + " "
print(output_string)