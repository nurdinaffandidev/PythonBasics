# Single quote
from Variables import firstName

singleQuoteString = 'This is a \'single\' quote string'
print(singleQuoteString)

# Double quote
doubleQuoteString = "This is a \"double\" quote string"
print(doubleQuoteString)

# Multiline single quote
multilineSingleQuoteString = '''
This is a multiline double quote sentence.
Hello world
Salam dunia
'''
print(multilineSingleQuoteString)

# Multiline double quote
multilineDoubleQuoteString = """ 
This is a multiline double quote sentence.
Hello world
Salam dunia
"""
print(multilineDoubleQuoteString)

# character index
index_string = "Python for beginners"
print("Character at index 0: " + index_string[0])
print("Character at index 1: " + index_string[1])
print("Character at index 2: " + index_string[2])
print("Character at index 3: " + index_string[3])
print("Character at index -1: " + index_string[-1])
print("Character at index -2: " + index_string[-2])
print("Character at index -3: " + index_string[-3])
print("Character at index 0 to 2: " + index_string[0:3])
print("Character at index 0 to ?: " + index_string[0:])
print("Character at index 1 to ?: " + index_string[1:])
print("Character at index ? to 4: " + index_string[:5])
print("Character at index ? to ?: " + index_string[:])

print("Character at index 1 to -1: " + index_string[1:-1])

# Formatted Strings
first = 'John'
last = 'Doe'
message = first + ' [' + last + '] is a coder' # string concatenation
print(message)
msg = f'{first} [{last}] is a coder' # formatted string
msg2 = "{}, {}"
print(msg)
print(msg2.format(first, last))

first_name = "Johan"
last_name = "Smith"
message2 = first_name + " [" + last_name + "] is a coder" # string concatenation
print(message2)
msg2 = f"{first_name} [{last_name}] is a coder" # formatted string
print(msg2)