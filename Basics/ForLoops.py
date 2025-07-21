# for loop String
print("for loop String:")
print("=====================")
for char in "Python":
    print(char)

# for loop break
print("\nfor loop break:")
print("=====================")
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

# for loop continue
print("\nfor loop continue:")
print("=====================")
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Skipped!")
        continue
    print(num)

# for loop list
print("\nfor loop list:")
print("=====================")
names = ["Mosh", "John", "Sarah"]
for name in names:
    print(name)

for num in [6, 7, 8, 9]:
    print(num)

# for loop range
print("\nfor loop range:")
print("=====================")
for num in range(0, 6):
    print(num)
print()
for num in range(10, 16):
    print(num)

# for loop range, step
print("\nfor loop range step:")
print("=====================")
for num in range(5, 10, 2):
    print(num)

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total = {total}")
total2 = sum(prices)
print(f"Total = {total2}")

# loop within a loop
print("\nloop within a loop:")
print("=====================")
for num in nums:
    for letter in 'abc':
        print(num, letter)