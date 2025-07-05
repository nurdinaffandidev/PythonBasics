import re

r"""
    Metacharacters are characters with a special meaning:
    
    Character	Description	                                        Example
    []	        A set of characters	                                "[a-m]"
    \	        Signals a special sequence                          "\d"
                (can also be used to escape special characters)
    .	        Any character (except newline character)	        "he..o"
    ^	        Starts with	                                        "^hello"
    $	        Ends with	                                        "planet$"
    *	        Zero or more occurrences	                        "he.*o"
    +	        One or more occurrences	                            "he.+o"
    ?	        Zero or one occurrences	                            "he.?o"
    {}	        Exactly the specified number of occurrences	        "he.{2}o"
    |	        Either or	                                        "falls|stays"
    ()	        Capture and group
    
    Note: In regular expressions, you should always use raw strings (r"") to avoid SyntaxWarning: invalid escape sequence '\ '.

"""
print()
# '[]':
print("'[]': Find all lower case characters alphabetically between 'a' and 'm'")
print("======================================================================")
txt = "The rain in Spain"
x = re.findall(r"[a-m]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'[]': Find all upper case characters alphabetically between 'A' and 'M'")
print("======================================================================")
txt = "THE rain in Spain"
x = re.findall(r"[A-M]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'[]': Find all characters alphabetically between 'A - M' and 'a - m'")
print("======================================================================")
txt = "THE rain in Spain"
x = re.findall(r"[A-Ma-m]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'[]': Find all characters alphabetically between 'A - Z','a - Z' and '0-9'")
print("======================================================================")
txt = "THE rain in Spain 0123456789"
x = re.findall(r"[a-zA-Z0-9]", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

# '\':
print("'\\': Find all digit characters")
print("======================================================================")
txt = "That will be 59 dollars"
x = re.findall(r"\d", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

print("'\\': Find all \" characters")
print("======================================================================")
txt = "That will be 59 \"dollars\""
x = re.findall(r"\"", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

# '.':
print("'.': #Search for a sequence that starts with \"he\", followed by two (any) characters, and an \"o\"")
print("======================================================================")
txt = "hello planet, this is tutorial hell"
x = re.findall(r"he..o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

# '$':
print("'$': Check if the string ends with 'planet'")
print("======================================================================")
txt = "hello planet"
x = re.findall(r"planet$", txt)
print(f"text = {txt}")
print(f"\"{txt}\" ends with 'planet'? = {True if x else False}", end="\n\n")

# '*':
print("'*': Search for a sequence that starts with \"he\", followed by 0 or more (any) characters, and an \"o\"")
print("======================================================================")
txt = "helllllloooo planet"
x = re.findall(r"he.*o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

txt = "hero planet"
x = re.findall(r"he.*o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

txt = "heo planet"
x = re.findall(r"he.*o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

# '+':
print("'+': Search for a sequence that starts with \"he\", followed by 1 or more (any) characters, and an \"o\"")
print("======================================================================")
txt = "hero planet"
x = re.findall(r"he.+o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

txt = "heo planet"
x = re.findall(r"he.+o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

# '?':
print("'?': Search for a sequence that starts with \"he\", followed by 0 or 1  (any) character, and an \"o\"")
print("======================================================================")
txt = "hero planet"
x = re.findall(r"he.?o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

txt = "hello planet"
x = re.findall(r"he.?o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

# '{}':
print("'{}': Search for a sequence that starts with \"he\", followed with exactly 2 (any) characters, and an \"o\"")
print("======================================================================")
txt = "hello planet"
x = re.findall(r"he.{2}o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

txt = "hero planet"
x = re.findall(r"he.{2}o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

txt = "helllo planet"
x = re.findall(r"he.{2}o", txt)
print(f"text = {txt}")
print(f"result = {x}", end="\n\n")

# '|':
print("'|': Check if the string contains either \"falls\" or \"stays\"")
print("======================================================================")
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall(r"falls|stays", txt)
print(f"text = {txt}")
print(f"text contains \"falls\" or \"stays\"? = {True if x else False}", end="\n\n")

txt = "The rain in Spain stays in the plain!"
x = re.findall(r"falls|stays", txt)
print(f"text = {txt}")
print(f"text contains \"falls\" or \"stays\"? = {True if x else False}", end="\n\n")

txt = "The rain in Spain is heavy!"
x = re.findall(r"falls|stays", txt)
print(f"text = {txt}")
print(f"text contains \"falls\" or \"stays\"? = {True if x else False}", end="\n\n")
