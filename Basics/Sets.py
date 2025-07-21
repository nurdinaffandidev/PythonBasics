# Sets - unordered, no duplicates
courses = {'History', 'Math', 'Physics', 'Chemistry', 'Physics'}
print(f"courses = {courses}")

# set cannot be access via index
print(f"\n# set cannot be access via index:")
print("==================================")
# print(courses[1]) # throws TypeError: 'set' object is not subscriptable
print(list(courses)[1]) # convert to list if accessing by index

# membership test
print(f"\n# membership test:")
print("==================================")
print('Math' in courses) # sets performs membership test faster than list and tuples

# intersection
print(f"\n# intersection:")
print("==================================")
art_courses = {'History', 'Art'}
print(f"courses: {courses}")
print(f"art courses: {art_courses}")
print(f"intersect courses: {courses.intersection(art_courses)}")

# difference
print(f"\n# difference:")
print("==================================")
print(f"courses: {courses}")
print(f"art courses: {art_courses}")
print(f"difference courses: {courses.difference(art_courses)}")

# union
print(f"\n# union:")
print("==================================")
print(f"courses: {courses}")
print(f"art courses: {art_courses}")
print(f"union courses: {courses.union(art_courses)}")


# empty set init
print(f"\n# empty set init:")
print("==================================")
# empty_set = {} # this isnt right, creates a dictionary
empty_set = set()
print(f"empty set: {empty_set}")