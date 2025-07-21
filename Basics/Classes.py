print("\nClass with no attributes")
print("=========================")

# Class with no attributes
class PointNoAttribute:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

    def __str__(self):
        return "Point object with no attributes declared in initializer"


point1 = PointNoAttribute()
print(f"point1 = <'type': {type(point1)}, 'object': {point1}>")
# adding attributes not declared in constructors
point1.x = 10
point1.y = 20
print(f"point1.x = {point1.x}")
print(f"point1.y = {point1.y}")
# calling object methods
point1.draw()
print()

point2 = PointNoAttribute()
# print(point2.x) # AttributeError as attribute 'x' not added

# ==============================================================================

print("\nClass with attributes")
print("=========================")

class Point:
    # Constructor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

    def __str__(self):
        return f"Point[x: {self.x}, y: {self.y}]"

point3 = Point(10, 20)
print(f"point3 = <'type': {type(point3)}, 'object': {point3}>")
print(f"point3.x = {point3.x}")
print(f"point3.y = {point3.y}\n")

# ==============================================================================

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

    def __str__(self):
        return f"Person[name: {self.name}]"


person1 = Person("John")
print(f"person1 = <'type': {type(person1)}, 'object': {person1}>")
print(f"person1.name = {person1.name}")
person1.talk()

person2 = Person("Bob Smith")
print(f"\nperson2 = <'type': {type(person2)}, 'object': {person2}>")
person2.talk()