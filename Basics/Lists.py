names = ["John", "Bob", "Mosh", "Mary", "Sarah"]
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])

print(names[2:]) # return new list
print(names[2:4]) # return new list
print(names)

numbers = [2, 10, 3, 4, 6, 7, 5, 9, 8, 1]
print(f"Largest number =  {max(numbers)}")
current_largest = numbers[0]
for num in numbers:
    current_largest = num if num > current_largest else current_largest
print(f"Largest number =  {current_largest}")

numbers.sort()
print(f"Largest number =  {numbers[-1]}")

print(f"Largest number =  {sorted(numbers)[-1]}")

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