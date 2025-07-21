print("\nappend:")
print("================")
numbers = [5, 5, 2, 1, 7, 4]
print(f"ori list: {numbers}")
numbers.append(20)
print(f"after append: {numbers}")

print("\ninsert:")
print("================")
print(f"ori list: {numbers}")
numbers.insert(1, 10)
print(f"after insert: {numbers}")

print("\ncount:")
print("================")
print(f"ori list: {numbers}")
print(f"number of 5s = {numbers.count(5)}")

print("\nremove:")
print("================")
print(f"ori list: {numbers}")
numbers.remove(5)
print(f"after remove: {numbers}")

print("\npop:")
print("================")
print(f"ori list: {numbers}")
popped_value = numbers.pop()
print(f"popped value = {popped_value}")
print(f"after pop: {numbers}")

print("\nindex:")
print("================")
print(f"first index of '5' = {numbers.index(5)}")
# print(numbers.index(3)) # results in ValueError: 3 is not in list
print(f"numbers contains '3': {3 in numbers}")

print("\nsort:")
print("================")
print(f"ori list: {numbers}")
numbers.sort(reverse=True)
print(f"after sort reverse: {numbers}")
numbers.sort()
print(f"after sort: {numbers}")

print("\nreverse:")
print("================")
print(f"ori list: {numbers}")
numbers.reverse()
print(f"after reverse: {numbers}")

print("\nsorted:")
print("================")
print(f"sorted copy of numbers: {sorted(numbers)}") # sorted() creates a copy
print(f"numbers: {numbers}")

print("\ncopy:")
print("================")
numbers_copy = numbers.copy()
numbers_copy.append("extra")
numbers.append(12)
print(f"numbers_copy: {numbers_copy}")
print(f"numbers: {numbers}")

print("\nclear:")
print("================")
print(f"ori list: {numbers}")
numbers.clear()
print(f"after clear: {numbers}")


"""
Exercise:
    Remove the duplicates in a list.
"""
print("\nexercise: Remove the duplicates in a list.")
print("================")
nums = [2, 2, 4, 6, 3, 4, 6, 1]
nums_unique_set = set(nums)
print(f"removed via set: {nums_unique_set}")
nums_unique_copy = []
for num in nums:
    if num not in nums_unique_copy:
        nums_unique_copy.append(num)
print(f"removed via loop: {nums_unique_copy}")