'''
Comparisons:
# Equals: ==
# Not equals: !=
# Greater than: >
# Lesser than: <
# Greater or equal: >=
# Lesser or equal: <=
# Object identity: is (same object in memory)

# and
# or
# not

False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example: '', (), []
# Any empty mapping. For example: '{}'
'''

is_hot = True
is_cold = True

if is_hot and not is_cold:
    print("It's a hot day")
elif is_cold and not is_hot:
    print("It's a cold day")
elif is_hot and is_cold:
    print("It's a confusing day")
else:
    print("It's a great day")


# Object identity test
print("\nObject identity test:")
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a == b : {a == b}")  # value equality
print(f"a is b : {a is b}")  # id equality
print(f"id a = {id(a)}")
print(f"id b = {id(b)}")

# False values
print("\nFalse values:")
# condition = False # return False
# condition = None # return False
# condition = 0 # return False
# condition = 10 # return True
# condition = '' # return False
# condition = 'some' # return True
# condition = [] # return False
# condition = [1,2] # return True
# condition = () # return False
# condition = (1,2) # return True
# condition = {} # return False
condition = {'key':'value'} # return True

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

'''
Exercise:
    Price of a house is $1M. 
    If buyer has good credit, they need to put down 10%.
    Otherwise, they need to put down 20%.
    Print down payment.
'''
has_good_credit = False

if has_good_credit:
    print(f"\nDown payment required = ${str(int(1_000_000 * 0.1))}")
else:
    print(f"\nDown payment required = ${str(int(1_000_000 * 0.2))}")