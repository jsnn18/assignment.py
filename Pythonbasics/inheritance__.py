class Person:
    def person_info(self):
        print("Name: Jeshika")
        print("Age: 20")


class Student(Person):
    def student_info(self):
        print("Course: Electronics")


class Teacher(Person):
    def teacher_info(self):
        print("Subject: Python")


student = Student()
teacher = Teacher()

print("Student Details")
student.person_info()
student.student_info()

print("\nTeacher Details")
teacher.person_info()
teacher.teacher_info()