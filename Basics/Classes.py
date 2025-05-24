class PointNoAttribute:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = PointNoAttribute()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = PointNoAttribute()
# print(point2.x) # AttributeError

# Constructor:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point3 = Point(10, 20)
print(point3.x)
print(point3.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

person1 = Person("John")
print(person1.name)
person1.talk()

person2 = Person("Bob Smith")
person2.talk()