class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass # python does not like empty class, need to add 'pass' statement


class Cat(Mammal):
    def purr(self):
        print("purr")

    # Override
    def walk(self):
        print("walk sneakily")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.purr()
cat1.walk()