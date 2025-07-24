'''
# program to illustrate public access modifier in a class
Public Access Modifier:
    - The members of a class that are declared public are easily accessible from any part of the program.
    - All data members and member functions of a class are public by default.
'''

class Geek:
    # constructor
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.geekAge)


if __name__ == "__main__":
    # creating object of the class
    obj = Geek("R2J", 20)

    # finding all the fields and methods which are present inside obj
    print("List of fields and methods inside obj:", dir(obj))

    # accessing public data member
    print("Name:", obj.geekName)

    # calling public member function of the class
    obj.displayAge()