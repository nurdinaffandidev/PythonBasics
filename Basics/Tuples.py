# Tuples are immutable
# can get only information of tuple object, cannot change
print("\nAccess value via index:")
print("==============================")
numbers = (1, 2, 3)
print(f"value at index 0 = {numbers[0]}")

# changing value of tuple will result in `TypeError`
# numbers[0] = 10 # will result in `TypeError: 'tuple' object does not support item assignment`

# Unpacking
print("\nUnpacking:")
print("==============================")
coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z = coordinates # shorthand for above
print(f"coordinates: {coordinates}")
print(f"x, y, z = {x, y, z}")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# empty tuple init
print("\nEmpty tuple init:")
print("==============================")
empty_tuple = ()
empty_tuple2 = tuple()
print(empty_tuple)
print(empty_tuple2)

'''
Immutability proof
'''
print("\nImmutability proof:")
print("==============================")
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