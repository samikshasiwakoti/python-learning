class Student:
    school = "AbC School"
    @classmethod
    def show(cls): # cls is used to access class variables
        print(cls.school)
Student.show()      