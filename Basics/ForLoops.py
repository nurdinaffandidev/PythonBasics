for char in "Python":
    print(char)

names = ["Mosh", "John", "Sarah"]
for name in names:
    print(name)

for num in range(0, 6):
    print(num)

for num in [6,7,8,9]:
    print(num)

for num in range(10, 16):
    print(num)

for num in range(5, 10, 2):
    print(num)

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total = {total}")
total2 = sum(prices)
print(f"Total = {total2}")