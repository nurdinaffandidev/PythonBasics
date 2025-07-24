'''
# program to illustrate protected access modifier in a class
Protected Access Modifier:
    - The members of a class that are declared protected are only accessible within the class where it is declared and its subclass.
    - To implement protected field or method, the developer follows a specific convention mostly by adding prefix to the variable or function name.
    - Popularly, a single underscore "_" is used to describe a protected data member or method of the class.
    - Note that the python interpreter does not treat it as protected data like other languages,
      it is only denoted for the programmers since they would be trying to access it using plain name instead of calling it using the respective prefix.
'''

# super class
class Student:
    # protected data members
    _name = None
    _metric_number = None
    _branch = None

    # constructor
    def __init__(self, name, metric_number, branch):
        self._name = name
        self._metric_number = metric_number
        self._branch = branch

    # protected member function
    def _display_metric_number_and_branch(self):
        # accessing protected data members
        print("Role:", self._metric_number)
        print("Branch:", self._branch)


# derived class
class ForeignStudent(Student):
    # constructor
    def __init__(self, name, metric_number, branch):
        Student.__init__(self, name, metric_number, branch)

    # public member function
    def display_details(self):
        # accessing protected data members of super class
        print("Name:", self._name)
        # accessing protected member functions of super class
        self._display_metric_number_and_branch()


if __name__ == "__main__":
    print("\nStudent class:")
    print("======================")
    stu = Student("Alpha", 1234567, "Computer Science")
    print(f"List of fields and methods inside Student Class:\n{dir(stu)}")

    # protected members and methods can be still accessed
    print(stu._name)
    stu._display_metric_number_and_branch()

    # Throws error: `AttributeError: 'Student' object has no attribute 'name'. Did you mean: '_name'?`
    # print(stu.name)
    # stu._display_metric_number_and_branch()

    print("\nForeignStudent class:")
    print("======================")
    # creating objects of the derived class
    foreign_stu = ForeignStudent("R2J", 1706256, "Information Technology")
    print(f"List of fields and methods inside ForeignStudent Class:\n{dir(foreign_stu)}")

    # calling public member functions of the class
    foreign_stu.display_details()