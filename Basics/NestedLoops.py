# (x,y) coordinates
for x in range(4):
    for y in range(4):
        print(f"({x},{y})")

'''
Exercise
    Print:
    xxxxx
    xx
    xxxxx
    xx
    xx
'''
numbers = [5,2,5,2,2]
for idx in range(len(numbers)):
    xs = numbers[idx]
    print("x" * xs)

print()

for x_count in numbers:
    print("x" * x_count)

print()

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)