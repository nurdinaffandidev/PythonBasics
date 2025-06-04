# Sets - unordered, no duplicates
courses = {'History', 'Math', 'Physics', 'Chemistry', 'Physics'}
print(courses)

# set cannot be access via index
# print(courses[1]) # throws TypeError: 'set' object is not subscriptable

# membership test
print('Math' in courses) # sets performs membership test faster than list and tuples

# intersection
art_courses = {'History', 'Art'}
print(courses.intersection(art_courses))

# difference
print(courses.difference(art_courses))

# union
print(courses.union(art_courses))

# empty set init
# empty_set = {} # this isnt right, creates a dictionary
empty_set = set()