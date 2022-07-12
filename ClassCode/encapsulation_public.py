class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute

std = Student("Steve", 25)
print(std.schoolName)
print(std.name)
print(std.age)