class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(f"This person's name is {self.name} and he is {self.age} years old")

class Student(Person):
    def __init__(self, name, age, nis, grade):
        super().__init__(name, age)
        self.nis = nis
        self.grade = grade

    def getInfo(self):
        print(f"This person's name is {self.name} and he is {self.age} years old, and he is in grade {self.grade}")


    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

person1 = Person("Ahmad", 30)
person1.getInfo()

Student1= Student("Beni", 16, "20211243", "10th")
Student1.getInfo()
Student1.study("Math")
