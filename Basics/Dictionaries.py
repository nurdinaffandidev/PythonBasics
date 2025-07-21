"""
name: John Smith
email: johnSmith@gmail.com
age: 30
"""
# empty dict
print("\nempty dict:")
print("==================")
empty_dict = {}
empty_dict2 = dict()
print(empty_dict)
print(empty_dict2)

# init dict
print("\ninit dict:")
print("==================")
new_dict = dict()
customer = {
    "name" : "John Smith",
    "email": "johnSmith@gmail.com",
    "age" : 30,
    "is_verified" : True,
    12 : 34
}
print(new_dict)
print(customer)

# get values from direct key access
print("\nget values from direct key access:")
print("=========================================")
print(f"key= \"name\" -> value= {customer["name"]}")
print(f"key= int(12) -> value= {customer[12]}")
# print(customer["birth_date"]) # KeyError: 'birth_date'
# print(customer["Name"]) # KeyError: 'Name'

# get values from key using dict.get('key')
print("\nget values from key using dict.get('key'):")
print("===============================================")
print(f"key= \"name\" -> value= {customer.get("name")}")
print(f"key= \"Name\" -> value= {customer.get("Name")}") # does not throw KeyError: 'Name', instead return None
print(f"key= \"Name\" -> value= {customer.get("Name", 'Not Found')}") # return default value 'Not Found'
print(f"key= \"birth_date\" -> value= {customer.get("birth_date", "Jan 1 1980")}") # 2nd param: default value
print(f"customer = {customer}")

# amend value of key
print("\namend value of key:")
print("===============================================")
customer["name"] = "Jack Doe"
print(f"key= \"name\" -> value= {customer.get("name")}")
print(f"customer = {customer}")


# add new key value
print("\nadd new key value:")
print("===============================================")
customer["birth_date"] = "Jan 1 1980"
print(f"key=\"birth_date\" -> value= {customer.get("birth_date")}")
print(f"customer = {customer}")

# update/add multiple key values
print("\nupdate/add multiple key values:")
print("===============================================")
customer.update({'name': 'Jane Doe', 'age': 29, 'email': 'janeDoe@gmail.com', 'phone': '555-55555'})
print(f"customer = {customer}")

# delete key and value
print("\ndelete key and value:")
print("===============================================")
print(f"key value to delete: key= \"age\" : value= {customer['age']}")
del customer['age']
print(f"customer = {customer}")

# pop key,value
print("\npop key,value:")
print("===============================================")
phone = customer.pop('phone')
print(f"popped value = {phone}")
print(f"customer = {customer}")

# get keys
print("\nget keys:")
print("===============================================")
print(f"keys from dict(customer) = {customer.keys()} (type: {type(customer.keys())})")

# get values
print("\nget values:")
print("===============================================")
print(f"values from dict(customer) = {customer.values()} (type: {type(customer.values())})")

# get items
print("\nget items:")
print("===============================================")
print(f"items from dict(customer) = {customer.items()} (type: {type(customer.items())})")
for item in customer.items():
    print(f"{type(item)} - {item}")

# iterate through key, value
print("\niterate through key, value:")
print("===============================================")
for key, value in customer.items():
    print(f"key= {key} : value={value}")

# access dict via index
print("\naccess dict via index")
print("===============================================")
print(f"item at index 0 = {list(customer.items())[0]}, type={type(list(customer.items())[0])}")


# Exercise: Print out input int value to literal word
print("\nExercise: Print out input int value to literal word:")
print("===============================================")
# phone = input("\nEnter a number: ") # uncomment to use input
phone = "12" # comment out to use input
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


# default dict (value: list()) example
print("\ndefaultdict:")
print("===============================================")
from collections import defaultdict
# using dictionary (list: need add key and instantiate empty list before append value)
normal_dict = {}
# normal_dict["a"].append(1)  # ❌ KeyError if "a" doesn't exist, need do extra checks
key = "a"
if key not in normal_dict:
    normal_dict[key] = []
normal_dict["a"].append(1)
print(normal_dict)

# using defaultdict from collections (list: append value directly, auto-instantiate empty list)
default_dict = defaultdict(list)
default_dict["a"].append(1)  # ✅ No error; "a" is initialized to []
print(default_dict)