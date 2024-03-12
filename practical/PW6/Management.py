import math as m
import numpy as np
import zipfile as zf
import pickle
from pathlib import Path
from Course import Course
from Student import Student

class Management:
    # initialize the student and course list
    def __init__(self):
        self.students = np.array([])
        self.courses = []

    # enter the student info
    def inputStudentInfo(self):
        studentNum = int(input("Please enter the number of students: ")) #need to add try except here
        for _ in range(studentNum):
            print("=================================")
            id = input("Please enter the Student ID: ")
            name = input("Please enter the Student name: ")
            dob = input("Please enter the Student's DOB: ")
            numpy_students = Student(id=id, name = name, dob = dob)
            self.students = np.append(self.students, numpy_students)

    # enter the course info
    def inputCourseInfo(self):
        courseNum = int(input("Please enter the number of courses: ")) #need to ask for try except here

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
        courseID = input("Please enter the Course ID: ") #need try except
        for course in self.courses:
            if courseID == course.id:
                score = float(input(f"Please enter the score for {courseID}: "))
            # else: 
            #     print("Invalid Course. ")
        # accessing each elements in students list
        for student in self.students:
            if studentID == student.id:
                student.setScore(courseID, score)

    # displaying all the scores:
    def displayScores(self):
        # studentID = input("Enter the Student ID: ")
        for course in self.courses:
            creditsDict = {course.id: course.credits}
            weightsDict = {course.id: course.weight}
        for student in self.students:
            # if student.id == studentID:
                scores = student.getScore()
                print("=================================")
                print(f"{student.id} - {student.name}: ")
                for course_id, score in scores.items():
                    print(f"{course_id}:{m.floor(score)}")
                student.calGPA(creditsDict=creditsDict, weightDict=weightsDict)
                print(f"GPA: {student.gpa}")
            # else:
                print("Invalid Student Credentials")
    # this is the how: https://docs.python.org/3/library/zipfile.html 
    # compression into a .dat file
    def zipFiles(self):
        studentsTxt = open('students.txt', 'w')
        for student in self.students:
            studentsTxt.writelines(f"{student.id}, {student.name}, {student.dob}") 
        studentsTxt.close()

        coursesTxt = open('courses.txt', 'w')
        for course in self.courses:
            coursesTxt.writelines(f"{course.id}, {course.name}, {course.weight}, {course.credits}")
        coursesTxt.close()

        marksTxt = open('marks.txt', 'w')
        for student in self.students:
            scores = student.getScore()
            marksTxt.writelines(f"{student.id}, {student.name}")
            for course_id, score in scores.items():
                marksTxt.writelines(f",{course_id}:{m.floor(score)}")
        marksTxt.close()

        path = Path("./student.dat")
        if path.is_file() != True:
            bigStudentInfo =  zf.ZipFile("student.dat", "w")
            bigStudentInfo.write("students.txt")
            bigStudentInfo.write("courses.txt")
            bigStudentInfo.write("marks.txt")
            bigStudentInfo.close()
        print("File is zipped successfully.")
    # pickling data into a file.
    def pickleFiles(self):
        with open('student.pickle', 'wb') as pickleData:
            pickle.dump(self, pickleData)
            print("File is pickled successfully.")

        path = Path("./student.pickle")
        if path.is_file() != True: #check if the file exists.
            bigStudentInfo =  zf.ZipFile("student.dat", "w") 
            bigStudentInfo.write("students.txt")
            bigStudentInfo.write("courses.txt")
            bigStudentInfo.write("marks.txt")
            bigStudentInfo.close()
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
                self.zipFiles()
                self.pickleFiles()
                print("Exited")
                break
            else:
                print("Invalid choice") 