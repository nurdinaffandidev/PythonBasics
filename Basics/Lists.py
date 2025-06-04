names = ["John", "Bob", "Mosh", "Mary", "Sarah"]
# Accessing list value by index
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])

# Slicing
print(names[2:]) # return new list
print(names[2:4]) # return new list
print(names)

# check item in list
print(f"2 in numbers = {'John' in names}")

# append
names.append("Josh1")
print(names)

# remove
names.remove("Josh1")
print(names)

# insert
names.insert(0, "Josh2")
print(names)

# pop
popped_name = names.pop(0)
print(f"popped name = {popped_name}")
print(names)

# extends list
names2 = ["Ali", "Baba"]
names.extend(names2)
print(names)

# sort
names.sort()
print(names)

# sort reverse
names.sort(reverse=True)
print(names)

# sorted copy
names_sorted = sorted(names)
print(names_sorted)
print(names)

# reverse sorted copy
names.sort()
names_reversed = sorted(names, reverse=True)
print(names_reversed)
print(names)

# join
names_joined = ', '.join(names)
print(names)
print(names_joined)

# split
list_split = names_joined.split(', ')
print(list_split)

# empty list init
empty_list = []
empty_list2 = list()

numbers = [2, 10, 3, 4, 6, 7, 5, 9, 8, 1]
print(f"Largest number =  {max(numbers)}")
current_largest = numbers[0]
for num in numbers:
    current_largest = num if num > current_largest else current_largest
print(f"Largest number =  {current_largest}")

numbers.sort()
print(f"Largest number =  {numbers[-1]}")

print(f"Largest number =  {sorted(numbers)[-1]}")

# sum items in list
print(f"sum of numbers = {sum(numbers)}")

# 2D Lists
print("\n2D Lists:")
"""
[
    1 2 3 
    4 5 6 
    7 8 9
]
"""
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
         ]
print(f"matrix[0][1] = {matrix[0][1]}")
matrix[0][1] = 20
print(f"after matrix[0][1] change = {matrix[0][1]}")

for row in matrix:
    for col in row:
        print(col)