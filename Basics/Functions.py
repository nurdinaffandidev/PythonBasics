'''
Note:
best coding practise: add 2 line breaks after functions
'''
def greet_user():
    print("Hi there!")
    print("Welcome aboard")


print("----- Start -----")
greet_user()
print("----- Finish -----")

# Parameters:
def greet_user_with_parameters(name = "Jenny"): # default: 'Jenny'
    print(f"Hi there {name}!")
    print("Welcome aboard")


print("\n----- Parameters start -----")
greet_user_with_parameters() # using default value
greet_user_with_parameters("John")

def greet_user_two_params(first_name: str, last_name: str) -> None: # only supported from Python 3.5+
# def greet_user_two_params(first_name, last_name): # this is an example of positional arguments
    print(f"Hi there {first_name} {last_name}!")
    print("Welcome aboard")


print("")
greet_user_two_params("John", "Smith")
print("----- Parameters finish -----")

# ================================================
# Keyword arguments:
print("\n----- Keyword arguments start -----")
greet_user_two_params(last_name="Smith", first_name="John") # this is an example of positional arguments
'''
Note: 
cannot have keyword arg followed by positional arg,
but can have positional arg followed by keyword arg.
'''
## greet_user_two_params(first_name="John", "Smith") #python complains
greet_user_two_params("John", last_name="Smith") #can have positional arg followed by keyword arg

# for numerical params, use keyword arguments to improve readability
def calculate_cost(total, shipping, discount):
    return (total + shipping) *  (1 - discount)


final_cost = calculate_cost(total=900, shipping=100, discount=0.2)
print(f"final cost = {final_cost}")
print("----- Keyword arguments finish -----")

# ================================================
print("\n----- *args, **kwargs start -----")
# *args, **kwargs: allowing us to accept an arbitrary number of positional/keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

print("\ndirect passing of *args, **kwargs:")
student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

print("\nincorrect passing of *args, **kwargs from list and dict:")
student_info(courses, info) # passing courses and info as a complete list and complete dict as positional arguments
print("\ncorrect passing of *args, **kwargs from list and dict: (via unpacking)")
student_info(*courses, **info) # unpack list values, unpack keyword values and passing as *args as individual positional arguments and **kwargs as individual keyword arguments

print("----- Keyword arguments finish -----")
# ================================================
# Return statement
'''
Note:
By default functions in python returns None
'''
def square(number):
    # return number * number
    return number ** 2

def square_no_return(number):
    print("print statement in function square_no_return:",number ** 2)
    # return None #default return

print("\n----- Return statement start -----")
print(f"Square of 3 = {square(3)}")
print(f"Square of 3 = {square_no_return(3)}")

print("----- Return statement finish -----")

# ================================================
# Creating a Reusable Function:
print("\n-----  Creating a Reusable Function: start -----")
'''
Note:
General rule of thumb, function should not worry about receiving input or printing output. 
'''
'''
message = input(">") #receiving input
words = message.split(" ")

emojis = {
    ":)" : "🙂",
    ":(" : "😔"
}
output_string = ""
for word in words:
    output_string += emojis.get(word, word) + " "

print(output_string) #printing output
'''

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "😔"
    }
    output_string = ""
    for word in words:
        if word == words[len(words) - 1]:
            output_string += emojis.get(word, word)
        else:
            output_string += emojis.get(word, word) + " "
    return output_string


message = input(">")
print(f"Massaged sentence: \"{emoji_converter(message)}\"")
print("-----  Creating a Reusable Function: finish -----")

# ================================================
# Exercise: Leap Year Function
print("\n-----  Exercise: Leap Year Function: start -----")
# Number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    """Return True if year is a leap year. False otherwise."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in a month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap_year(year):
        return 29

    return month_days[month]


print(is_leap_year(2017))
print(is_leap_year(2020))
print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
print("-----  Exercise: Leap Year Function: finish -----")