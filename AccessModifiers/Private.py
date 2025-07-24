'''
# program to illustrate private access modifier in a class
Private Access Modifier:
    - The members of a class that are declared private are accessible within the class only,
      private access modifier is the most secure access modifier.
    - Data members of a class are declared private by adding a double underscore '__' symbol before the data member of that class.
'''

class Teacher:
    # private members
    __name = None
    __id = None
    __branch = None

    # constructor
    def __init__(self, name, id, branch):
        self.__name = name
        self.__id = id
        self.__branch = branch

    # private member function
    def __display_details(self):
        # accessing private data members
        print("Name:", self.__name)
        print("ID:", self.__id)
        print("Branch:", self.__branch)

    # public member function
    def access_private_details(self):
        # accessing private member function
        self.__display_details()


if __name__ == "__main__":
    # creating object
    teacher = Teacher("R2J", 1706256, "Information Technology")

    print(f"List of fields and methods inside ForeignStudent Class:\n{dir(teacher)}")
    print("")

    # Throws error `AttributeError`
    # teacher.__name # AttributeError: 'Teacher' object has no attribute '__name'
    # teacher.__id
    # teacher.__branch
    # teacher.__display_details()

    # To access private members of a class via name mangling syntax (Not recommended for regular use)
    teacher._Teacher__name  # 'R2J'
    teacher._Teacher__id  # 1706256
    teacher._Teacher__branch  # 'Information Technology'
    teacher._Teacher__display_details()

    print("")
    # calling public member function of the class
    teacher.access_private_details()