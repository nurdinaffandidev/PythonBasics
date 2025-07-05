import re
r"""
Character	Description	                                                                                    Example
\A	        Returns a match if the specified characters are at the beginning of the string	                "\AThe"	

\b	        Returns a match where the specified characters are at the beginning or at the end of a word     r"\bain"
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"ain\b"

\B	        Returns a match where the specified characters are present,                                     r"\Bain"
            but NOT at the beginning (or at the end) of a word                                              r"ain\B"	
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")	

\d	        Returns a match where the string contains digits (numbers from 0-9)	                            "\d"
	
\D	        Returns a match where the string DOES NOT contain digits	                                    "\D"
	
\s	        Returns a match where the string contains a white space character	                            "\s"
	
\S	        Returns a match where the string DOES NOT contain a white space character	                    "\S"
	
\w	        Returns a match where the string contains any word characters                                   "\w"
            (characters from a to Z, digits from 0-9, and the underscore _ character)
            		
\W	        Returns a match where the string DOES NOT contain any word characters	                        "\W"
	
\Z	        Returns a match if the specified characters are at the end of the string	                    "Spain\Z"
"""

print()
# '\A':
print(r"'\A': " + "Check if the string starts with \"The\"")
print("======================================================================")
txt = "The rain in Spain"
x = re.findall(r"\AThe", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text starts with \"The\"? = {True if x else False}", end="\n\n")

txt = "Raining in Spain. What the.."
x = re.findall(r"\AThe", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text starts with \"The\"? = {True if x else False}", end="\n\n")

# \b
print(r"'\b': " + "Check if \"ain\" is present at the beginning of a WORD")
print("======================================================================")
txt = "I say ain't got time for that"
x = re.findall(r"\bain", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at beginning of any word? = {True if x else False}", end="\n\n")

txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at beginning of any word? = {True if x else False}", end="\n\n")

print(r"'\b': " + "Check if \"ain\" is present, but NOT at the end of a word")
print("======================================================================")
txt = "It is raining in Spain"
x = re.findall(r"ain\B", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at any word but does not end with \"ain\"? = {True if x else False}", end="\n\n")

txt = "The rain in Spain"
x = re.findall(r"ain\B", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at any word but does not end with \"ain\"? = {True if x else False}", end="\n\n")

# \B
print(r"'\B': " + "Check if \"ain\" is present, but NOT at the beginning of a word")
print("======================================================================")
txt = "The rain in Spain"
x = re.findall(r"\Bain", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at any word but does begin with \"ain\"? = {True if x else False}", end="\n\n")

txt = "I say ain't it cool"
x = re.findall(r"\Bain", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at any word but does begin with \"ain\"? = {True if x else False}", end="\n\n")

print(r"'\B': " + "Check if \"ain\" is present, but NOT at the end of a word")
print("======================================================================")
txt = "The rain in Spain"
x = re.findall(r"ain\B", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at any word but does end with \"ain\"? = {True if x else False}", end="\n\n")

txt = "It is raining heavily in Spain"
x = re.findall(r"ain\B", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains \"ain\" at any word but does end with \"ain\"? = {True if x else False}", end="\n\n")

# \d
print(r"'\d': " + "Check if the string contains any digits (numbers from 0-9)")
print("======================================================================")
txt = "The temperature in Spain is 42 degree celsius"
x = re.findall(r"\d", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains any digits? = {True if x else False}", end="\n\n")

txt = "The rain in Spain"
x = re.findall(r"\d", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains any digits? = {True if x else False}", end="\n\n")

# \D
print(r"'\D': " + "Return a match at every no-digit character")
print("======================================================================")
txt = "The temp is 42 deg"
x = re.findall(r"\D", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains any non-digits characters? = {True if x else False}", end="\n\n")

# \s
print(r"'\s': " + "Returns a match where the string contains a white space character")
print("======================================================================")
txt = "The rain in Spain"
x = re.findall(r"\s", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains whitespace characters? = {True if x else False}", end="\n\n")

txt = "MyNameJeff"
x = re.findall(r"\s", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains whitespace characters? = {True if x else False}", end="\n\n")

# \S
print(r"'\S': " + "Return a match at every NON white-space character")
print("======================================================================")
txt = "The rain in Spain"
x = re.findall(r"\S", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains whitespace characters? = {True if x else False}", end="\n\n")

txt = "      "
x = re.findall(r"\S", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains whitespace characters? = {True if x else False}", end="\n\n")

# \w
print(r"'\w': " + "Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)")
print("======================================================================")
txt = "The rain in Spain_123"
x = re.findall(r"\w", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains characters [a-zA-Z0-9]? = {True if x else False}", end="\n\n")

# \W
print(r"'\W': " + "Return a match at every NON word character (characters NOT between a and Z. Like \"!\", \"?\" white-space etc.)")
print("======================================================================")
txt = "The **rain** in Spain_123?!"
x = re.findall(r"\W", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text contains NON word characters? = {True if x else False}", end="\n\n")

# \Z
print(r"'\Z': " + "Check if the string ends with \"Spain\"")
print("======================================================================")
txt = "The rain in Spain"
x = re.findall(r"Spain\Z", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text ends with \"Spain\"? = {True if x else False}", end="\n\n")

txt = "The rain in Spain is heavy"
x = re.findall(r"Spain\Z", txt)
print(f"text = {txt}")
print(f"result = {x}")
print(f"text ends with \"Spain\"? = {True if x else False}", end="\n\n")
