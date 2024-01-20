class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.__score = {}
    def setScore(self, course_id, score):
        self.__score[course_id] = score

    def displayInfo(self):
        print(f"""Student ID: {self.id} 
        Student name: {self.name} 
        DOB: {self.dob} """)
class Course:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        # self.studentNumber = studentNumber
    def displayInfo(self):
        print(f""" --------------
        Course ID: {self.__id} 
        Course Name: {self.name}""")
        
students = []
courses = {}

studentsNumber = int(input("Number of students: "))
for _ in range(studentsNumber):
    id = int(input("Student ID: "))
    name = input("Student Name: ")
    dob = input("DOB: ")
    students.append(Student(id, name, dob))

coursesNumber = int(input("Number of courses: "))
for _ in range(coursesNumber):
        code = input("Course ID: ")
        name = input("Course Name: ")
        courses[code] = name

print("-------Score insertion-------")

id = int(input("Student ID: "))
course_code = input("Course ID: ")
score = int(input("Score: "))
for student in students:
    if student.id == id:
        student.setScore(course_code, score)


for student in students:
    student.displayInfo()

for course in courses:
    student.displayInfo()

id = int(input("Student ID: "))
for student in students:
    if student.id == id:
        print(f"Student {student.id} scored {student.score}")