# Tuples are immutable
# can get only information of tuple object, cannot change
numbers = (1, 2, 3)
print(numbers[0])

# numbers[0] = 10 # will result in `TypeError: 'tuple' object does not support item assignment`

# Unpacking
coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z = coordinates # shorthand for above
print(x, y, z)

list_coordinates = [4, 5, 6]
x, y, z = list_coordinates
print(x, y, z)


# empty tuple init
empty_tuple = ()
empty_tuple2 = tuple()

'''
Mutability proof
'''

# Mutable
list_1 =['History', 'Math', 'Science']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Science')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art' # will result in `TypeError: 'tuple' object does not support item assignment`
# print(tuple_1)
# print(tuple_2)