import math as m
import numpy as np
from Course import Course
from Student import Student

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
            weight = float(input("Please enter the weight of the course: "))
            credits = int(input("Please enter the credits of the course: "))
            self.courses.append(Course(id=id, name = name, weight= weight, credits=credits))

    # displaying the overall information
    def displayInfo(self):
        print("\n---Displaying Information---")
        for course in self.courses:
            print("=================================")
            course.displayInfo()
        for student in self.students:
            print("=================================")
            student.displayInfo()

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
        for course in self.courses:
            creditsDict = {course.id: course.credits}
        for course in self.courses:
            weightsDict = {course.id: course.weight}
        for student in self.students:
            if student.id == studentID:
                scores = student.getScore()
                print("=================================")
                print(f"{student.id} - {student.name}: ")
                for course_id, score in scores.items():
                    print(f"{course_id}:{m.floor(score)}")
                student.calGPA(creditsDict=creditsDict, weightDict=weightsDict)
                print(f"GPA: {student.gpa}")

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