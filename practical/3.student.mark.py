import math
import numpy as np
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.__score = []
        self.__gpa = None
    def setScore(self, course_id:int, score):
        self.__score[course_id] = score
    def getScore(self):
        return self.__score
    def displayInfo(self):
        print(f"""Student ID: {self.id}
        Student name: {self.name}
        DOB: {self.dob}""")
    def calGPA(self, score):
        sum = 0
        for i in range(len(self.__score)):
            sum += self.__score[i]
            if i+1 == len(self.__score):
                self.__gpa = sum/len(self.__score)
        return self.__gpa

class Course:
    def __init__(self, id:int, name):
        self.__id = id
        self.name = name
        # self.studentNumber = studentNumber
    def displayInfo(self):
        print(f""" --------------
        Course ID: {self.__id+1}
        Course Name: {self.name}""")
        
students = np.array([])
# courses = {}
courses = []

# INPUT STUDENTS INFO 
studentsNumber = int(input("Number of students: "))
for _ in range(studentsNumber):
    # id = int(input("Student ID: "))
    id = input("Student ID: ")
    name = input("Student Name: ")
    dob = input("DOB: ")
    students = np.append(students,Student(id, name, dob))

# INPUT COURSES INFO
print("-----------------------------")
coursesNumber = int(input("Number of courses: "))
for _ in range(coursesNumber):
        code = int(input("Course Code: "))
        name = input("Course Name: ")
        courses[code-1] = Course(code, name)

# INSERTING SCORES
print("-------Score insertion-------")
for _ in range(studentsNumber):
    # id = int(input("Student ID: "))
    id = input("Student ID: ")
    course_code = int(input("Course Code: "))
    score = float(input("Score: "))
    for student in students:
        # while id != students[student].id:
        #     id = input("Student ID: ")
        if student.id == id:
            student.setScore(course_code, math.floor(score))
            

for student in students:
    student.displayInfo()

for course in courses.values():
    course.displayInfo()

# id = int(input("Student ID: "))
# for student in students:
#     if student.id == id:
#         print(f"Student {student.id} scored {student.score}")

# DISPLAYING THE GPA   
for student in students:
    student.calGPA(student.getScore())
    
id = input("Student ID: ")
for student in students:
    if student.id == id:
        student.displayInfo()
        print(f"Scores: {student.getScore()}")
        print(f"GPA: {student.getGPA()}")


# Display students and their GPAs
for student in students:
    student.displayInfo()
    print(f"GPA: {student.getGPA()}")
