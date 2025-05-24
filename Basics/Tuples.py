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