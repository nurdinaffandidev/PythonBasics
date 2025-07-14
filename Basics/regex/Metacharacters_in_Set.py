r"""
    List of all regular expression metacharacters (special characters) that behave specially inside [] character classes in regex

    Character	Description	                                Example
    ^	        Negation	                                "[^a-z]" # any char that is not a lowercase letter
    -	        Range                                       "[a-z]" # all lowercase letters
                                                            "[A-Z]" # all uppercase letters
                                                            "[0-9]" # all digits
                                                            "[a-zA-Z-0-9]" # all letters and digits
    \	        Escapes special characters inside a set.    "[\^]" # matches a literal caret (^)
                                                            "[\-]" # matches a literal dash (-)
                                                            "[\\]" # matches a literal backslash (\)
    ]	        End of character class                      "[]a]" # matches either a ']' or 'a'
                                                            "[^\]]" # matches anything except a literal ']'

    Note: Characters like . * + are not metacharacters inside [].
          [.*+]   # Matches a literal '.', '*', or '+'
"""

import re


print()
# '^':
print("'^': Find all char except vowels")
print("======================================================================")
txt = "banana"
x = re.findall(r"[^aeiou]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'^': Exclude digits")
print("======================================================================")
txt = "abc123xyz"
x = re.findall(r"[^0-9]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'^': Exclude all letters")
print("======================================================================")
txt = "C0d3!ing!"
x = re.findall(r"[^a-zA-Z]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")


# '-':
print("'-': Find lowercased letters")
print("======================================================================")
txt = "ABCdefXYZ"
x = re.findall(r"[a-z]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'-': Find digits between 0 - 5")
print("======================================================================")
txt = "9876543210"
x = re.findall(r"[0-5]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'-': Find all letters")
print("======================================================================")
txt = "123@#ABCabc"
x = re.findall(r"[a-zA-Z]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")


# '\':
print("'\\': Find literal backslashes")
print("======================================================================")
txt = "a\\b\\c"
x = re.findall(r"[\\]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'\\': Find literal caret")
print("======================================================================")
txt = "x^y"
x = re.findall(r"[\^]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'\\': Find literal dash")
print("======================================================================")
txt = "1-2-3"
x = re.findall(r"[\-]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")


# ']':
print("']': Matches literal ']'")
print("======================================================================")
txt = "a]b]c"
x = re.findall(r"[]]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("']': Matches everything except ']'")
print("======================================================================")
txt = "a]b]c"
x = re.findall(r"[^]]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("']': Matches 'a' and ']'")
print("======================================================================")
txt = "a]b]c"
x = re.findall(r"[a\]]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("., *, +: Examples for '.', '*', '+'")
print("======================================================================")
txt = "2*3+4.5"
x = re.findall(r"[.*+]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

txt = "c*d+e"
x = re.findall(r"[a-z*]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")