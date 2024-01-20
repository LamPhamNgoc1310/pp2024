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
    def __init__(self, id, name, studentNumber):
        self.id = id
        self.name = name
        # self.studentNumber = studentNumber
    def displayInfo(self):
        print(f""" --------------
              Course ID: {self.id} 
              Course Name: {self.name}""")
        
students = []
courses = {}

studentsNumber = int(input("Number of students: "))
for _ in range(studentsNumber):
    id = int(input("Student ID: "))
    name = input("Student Name: ")
    dob = input("DOB: ")
    students.append(Student(id, name, dob))