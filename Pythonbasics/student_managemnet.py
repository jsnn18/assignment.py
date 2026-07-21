class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("\nStudent Information")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)

    def update(self):
        self.name = input("Enter New Name: ")
        self.age = input("Enter New Age: ")
        self.course = input("Enter New Course: ")
        print("Student Information Updated!")


name = input("Enter Student Name: ")
age = input("Enter Age: ")
course = input("Enter Course: ")

student1 = Student(name, age, course)

print("\nOriginal Information")
student1.display()

choice = input("\nDo you want to update the information? (yes/no): ")

if choice.lower() == "yes":
    student1.update()

print("\nUpdated Information")
student1.display()