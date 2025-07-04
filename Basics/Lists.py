names = ["John", "Bob", "Mosh", "Mary", "Sarah"]
# Accessing list value by index
print("Accessing list value by index:")
print("==============================")
print(names[0])
print(names[2])
print(names[-1])
print(names[-2], end="\n\n")

# Slicing
print("Slicing:")
print("==============================")
print(names[2:]) # return new list
print(names[2:4]) # return new list
print(names, end="\n\n")

# check item in list
print("Check item in list:")
print("==============================")
print(f"John in names = {'John' in names} \n")

# append
print("Append:")
print("==============================")
names.append("Josh1")
print(names, end="\n\n")

# remove
print("Remove:")
print("==============================")
names.remove("Josh1")
print(names, end="\n\n")

# insert
print("Insert:")
print("==============================")
names.insert(0, "Josh2")
print(names, end="\n\n")

# pop
print("Pop:")
print("==============================")
popped_name = names.pop(0)
print(f"popped name = {popped_name}")
print(names, end="\n\n")

# extends list
print("Extends:")
print("==============================")
names2 = ["Ali", "Baba"]
names.extend(names2)
print(names, end="\n\n")

# sort
print("Sort:")
print("==============================")
names.sort()
print(names, end="\n\n")

# sort reverse
print("Reverse sort:")
print("==============================")
names.sort(reverse=True)
print(names, end="\n\n")

# sorted copy
print("Sorted copy:")
print("==============================")
names_sorted = sorted(names)
print(f"names_sorted: {names_sorted} --> copy of names, sorted")
print(f"names: {names} --> remains same", end="\n\n")

# reverse sorted copy
print("Reverse sorted copy:")
print("==============================")
names.sort()
names_reversed = sorted(names, reverse=True)
print(names_reversed)
print(names, end="\n\n")

# join
print("Join:")
print("==============================")
names_joined = ', '.join(names)
print(names)
print(names_joined, end="\n\n")

# split
print("Split:")
print("==============================")
list_split = names_joined.split(', ')
print(list_split, end="\n\n")

# empty list init
print("Empty list init:")
print("==============================")
empty_list = []
empty_list2 = list()
print(empty_list)
print(empty_list2, end="\n\n")

# finding largest number using built-in function max
print("Finding largest number using built-in function max:")
print("==============================")
numbers = [2, 10, 3, 4, 6, 7, 5, 9, 8, 1]
print(f"Largest number =  {max(numbers)} \n")

# finding largest number using for loop
print("Finding largest number using for loop:")
print("==============================")
current_largest = numbers[0]
for num in numbers:
    current_largest = num if num > current_largest else current_largest
print(f"Largest number =  {current_largest}\n")

# finding largest number using sort
print("Finding largest number using sort:")
print("==============================")
numbers.sort()
print(f"Largest number =  {numbers[-1]}")
print(f"Largest number =  {sorted(numbers)[-1]}\n")

# sum items in list
print("Sum items in list:")
print("==============================")
print(f"sum of numbers = {sum(numbers)}\n")

# 2D Lists
print("2D list:")
print("==============================")
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
    print(row)