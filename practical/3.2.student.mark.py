import math as m
import numpy as np

# The Student class
class Student:
    def __init__(self, id:str, name:str, dob:int):
        self.id = id
        self.name = name
        self.dob = dob
        self.__score = {}
        self.gpa = 0
    def setScore(self, course_id, score):
        self.__score[course_id] = score
    def getScore(self):
        return self.__score
    def displayInfo(self):
        print(f"---------{self.id} - {self.name} - {self.dob} -{self.gpa}---------")
    def calGPA(self, creditsDict):
        totalScore = 0
        totalCred = 0
        for course_id, score in self.__score.items():
            if course_id in creditsDict:
                totalGpa += score * creditsDict[course_id]
                totalCred += creditsDict[course_id]
        return totalScore / totalCred

# The Course class 
class Course:
    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name
        self.credits = {}
    def displayInfo(self):
        print(f"---------{self.id} - {self.name}---------")
    
class Management:
    # initialize the student and course list
    def __init__(self):
        self.students = np.array([])
        self.courses = []

    # enter the student info
    def inputStudentInfo(self):
        studentNum = int(input("Please enter the number of students: "))
        for _ in range(studentNum):
            print("=================================")
            id = input("Please enter the Student ID: ")
            name = input("Please enter the Student name: ")
            dob = input("Please enter the Student's DOB: ")
            numpy_students = Student(id=id, name = name, dob = dob)
            self.students = np.append(self.students, numpy_students)

    # enter the course info
    def inputCourseInfo(self):
        courseNum = int(input("Please enter the number of courses: "))
        for _ in range(courseNum):
            print("=================================")
            id = input("Please enter the Course ID: ")
            name = input("Please enter the Course name: ")
            self.courses.append(Course(id=id, name = name))

    # displaying the overall information
    def displayInfo(self):
        print("\n---Displaying Information---")
        for student in self.students:
            print("=================================")
            student.displayInfo()
        for course in self.courses:
            print("=================================")
            course.displayInfo()
    
    # inputing the scores in the list
    def inputScore(self):
        print("=================================")
        studentID = input("Please enter the Student ID: ")
        courseID = input("Please enter the Course ID: ")
        score = float(input(f"Please enter the score for {courseID}: "))
        # accessing each elements in students list
        for student in self.students:
            if studentID == student.id:
                student.setScore(courseID, score)

    # displaying all the scores:
    def displayScores(self):
        studentID = input("Enter the Student ID: ")
        for student in self.students:
            if student.id == studentID:
                scores = student.getScore()
                print("=================================")
                print(f"{student.id} - {student.name}: ")
                for course_id, score in scores.items():
                    print(f"{course_id}:{m.floor(score)}")

    # make colors

    def userChoices(self): 
        while True:
            print("""
                    ==============================================
                  ||0. Quit                                       ||
                  ||1. Entering Students Information              ||
                  ||2. Entering Courses Information               ||
                  ||3. Entering scores                            ||
                  ||4. Display students and courses information   ||
                  ||5. Displaying the scores                      ||
                    ==============================================
                  """)
            choice = input("Choose something...")
            if choice == "1":
                self.inputStudentInfo() 
            elif choice == "2":
                self.inputCourseInfo()
            elif choice == "3":
                self.inputScore()
            elif choice == "4":
                self.displayInfo()
            elif choice == "5":
                self.displayScores()
            elif choice == "0":
                print("Exited")
                break
            else:
                print("Invalid choice")

# main
main = Management()
main.userChoices()