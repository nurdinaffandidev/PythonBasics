"""
name: John Smith
email: johnSmith@gmail.com
age: 30
"""
# empty dict
empty_dict = {}
empty_dict2 = dict()

# init dict
new_dict = dict()
customer = {
    "name" : "John Smith",
    "email": "johnSmith@gmail.com",
    "age" : 30,
    "is_verified" : True,
    12 : 34
}

# get values from key
print("get values from key:")
print(customer["name"])
print(customer[12])
# print(customer["birth_date"]) # KeyError: 'birth_date'
# print(customer["Name"]) # KeyError: 'Name'

# get values from key using dict.get('key')
print("\nget values from key using dict.get('key'):")
print(customer.get("name"))
print(customer.get("Name")) # does not throw KeyError: 'Name', instead return None
print(customer.get("Name", 'Not Found')) # return default value 'Not Found'
print(customer.get("birth_date", "Jan 1 1980")) # 2nd param: default value
print(customer)

# amend value of key
customer["name"] = "Jack Doe"
print("\namend value of key:")
print(customer)


# add new key value
customer["birth_date"] = "Jan 1 1980"
print("\nadd new key value:")
print(customer)

# update/add multiple key values
customer.update({'name': 'Jane Doe', 'age': 29, 'email': 'janeDoe@gmail.com', 'phone': '555-55555'})
print("\nupdate multiple key values:")
print(customer)

# delete key and value
del customer['age']
print("\ndelete key,value:")
print(customer)

# pop key,value
phone = customer.pop('phone')
print("\npop key,value:")
print(phone)
print(customer)

# get keys
print("\nget keys:")
print(customer.keys())

# get values
print("\nget values:")
print(customer.values())

# get items
print("\nget items:")
for item in customer.items():
    print(f"{type(item)} - {item}")

# iterate through key, value
print("\niterate through key, value:")
for key, value in customer.items():
    print(f"key= {key} : value={value}")

# Exercise: Print out input int value to literal word
phone = input("\nEnter a number: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}

output_string = ""
for char in phone:
    output_string += digits_mapping.get(char, "Number not found!") + " "
print(output_string)