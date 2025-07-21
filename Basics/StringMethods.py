course_str = "Python for Beginners"

# len
print(f"\n# len:")
print("====================")
print(f"string = {course_str}")
print(f"length of string = {len(course_str)}") # len() general purpose function

# upper
print(f"\n# upper:")
print("====================")
print(f"string = {course_str}")
print(f"string upper = {course_str.upper()}")

# lower
print(f"\n# lower:")
print("====================")
print(f"string = {course_str}")
print(f"string lower = {course_str.lower()}")

# capitalize
print(f"\n# capitalize:")
print("====================")
print(f"string = {course_str}")
print(f"string capitalize = {course_str.capitalize()}")

# title
print(f"\n# title:")
print("====================")
print(f"string = {course_str}")
print(f"string title = {course_str.title()}")

# find
print(f"\n# find:")
print("====================")
print(f"string = {course_str}")
print(f"index of 'o' = {course_str.find('o')}") # index 4
print(f"index of Beginners' = {course_str.find("Beginners")}") # index 11

# replace
print(f"\n# replace:")
print("====================")
print(f"string = {course_str}")
replaced_char = course_str.replace("P", "J")
print(f"replaced 'P' with 'J': {replaced_char}")
replaced_word = course_str.replace("Beginners", "Pros")
print(f"replaced 'Beginners' with 'Pros': {replaced_word}")

# split
print(f"\n# split:")
print("====================")
course_str_split_list = course_str.split(" ") # split to list
print(f"split by \" \": {course_str_split_list}")

print(f"\"python\" in split list = {"python" in course_str}" )
print(f"\"Python\" in split list = {"Python" in course_str}" )

# rstrip
print(f"\n# rstrip:")
print("====================")
print(f"string = {course_str + "zzzzz"}")
print(f"string rstrip = { course_str.rstrip("z")}")

# rstrip
print(f"\n# lstrip:")
print("====================")
print(f"string = {"zzzzz" + course_str}" )
print(f"string lstrip = {course_str.lstrip("z")}")

# zfill
print(f"string = {course_str}, length = {len(course_str)} ")
print(f"string zfill = {course_str.zfill(25)}, length = {len(course_str.zfill(25))}")

# string.upper()
# string.lower()
# string.capitalize()
# string.title()
# string.find()
# string.replace()
# "..." in string
