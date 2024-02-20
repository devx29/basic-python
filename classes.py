#class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.school = "LES"
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def school_name(self):
        return self.school
    
student_1 = Student('Harsh', 28)
student_2 = Student('Krish', 26 )

print(f"Student {student_1.get_name().capitalize()} is {student_1.get_age()} years old!")
print(f"Student {student_2.get_name().capitalize()} is {student_2.get_age()} years old!") 

class ElementarySchool(Student):
    pass

class HighSchool(Student):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa
    
student_3 = ElementarySchool("Jane", 9)
student_4 = HighSchool("Jim", 15, 3.68)

print(f"Student {student_3.get_name().capitalize()} is {student_3.get_age()} years old!")
print(f"Student {student_4.get_name().capitalize()} is {student_4.get_age()} years old with a GPA of {student_4.get_gpa()}!")

for x in (student_1, student_2, student_3, student_4):
    print(x.get_name())
    