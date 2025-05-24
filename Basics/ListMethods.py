numbers = [5, 5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(1, 10)
print(numbers)

print(f"number of 5s = {numbers.count(5)}")

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(f"first index of '5' = {numbers.index(5)}")
# print(numbers.index(3)) # results in ValueError: 3 is not in list
print(f"numbers contains '3': {3 in numbers}")

numbers.sort()
print(f"sorted numbers: {numbers}")

numbers.reverse()
print(f"reversed numbers: {numbers}")

print(f"sorted copy of numbers: {sorted(numbers)}")
print(f"numbers: {numbers}")

numbers_copy = numbers.copy()
numbers.append(12)
print(f"numbers_copy: {numbers_copy}")
print(f"numbers: {numbers}")

numbers.clear()
print(numbers)

"""
Exercise:
    Remove the duplicates in a list.
"""
nums = [2, 2, 4, 6, 3, 4, 6, 1]
nums_unique_set = set(nums)
print(nums_unique_set)
nums_unique_copy = []
for num in nums:
    if num not in nums_unique_copy:
        nums_unique_copy.append(num)
print(nums_unique_copy)