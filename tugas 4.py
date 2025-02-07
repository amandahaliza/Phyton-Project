class Student:
    name = ""
    grade = ""

    def __init__ (self, student_name, student_grade):
        self.name = student_name
        self.grade = student_grade

    def study (self, subject):
         print(f"{self.name} is in grade {self.grade}, currently studying {subject} subject")

student1 = Student("amanda", "12")

student1.study("math")
