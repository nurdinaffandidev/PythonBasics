import re

"""
    findall(): Returns a list containing all matches
    search():  Returns a Match object if there is a match anywhere in the string
    split():   Returns a list where the string has been split at each match
    sub():	   Replaces one or many matches with a string
"""

# findall: returns a list containing all matches.
print("findall:")
print("=========================")
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(f"{x}\n'findall' function returns type = {type(x)}", end="\n\n")

# findall, no match:
print("findall, no match:")
print("=========================")
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x, end="\n\n")

# search: function searches the string for a match, and returns a Match object if there is a match.
print("search:")
print("=========================")
txt = "The rain in Spain, rain"
x = re.search("rain", txt)
print(f"{x}\n'search' function returns type = {type(x)}")
print(f"The first \"{x.group()}\" word is located in index={x.start()} through index={x.end()}", end="\n\n")

# search, no match:
print("search, no match:")
print("=========================")
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x, end="\n\n")

# split (similar to string split): returns a list where the string has been split at each match
print("split:")
print("=========================")
txt = "The rain in Spain"
x = re.split(" ", txt)
print(f"regex split: {x}\n'split' function returns type = {type(x)}")

y = txt.split(" ")
print(f"string split: {y}", end="\n\n")

# split (controlling the amount of splits):
print("split (controlling the amount of splits):")
print("=========================")
txt = "The rain in Spain"
x = re.split(" ", txt, 1)
print(x, end="\n\n")

# sub: replaces one or many matches with a string
print("sub:")
print("=========================")
txt = "The rain in Spain"
x = re.sub(" ", "9", txt)
print(x, end="\n\n")

# sub (controlling number of replacements):
print("sub (controlling number of replacements):")
print("=========================")
txt = "The rain in Spain"
x = re.sub(" ", "9", txt, 2)
print(x)