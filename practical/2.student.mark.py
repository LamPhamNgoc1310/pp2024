
# The Student class
class Student:
    def __init__(self, id:str, name:str, dob:int):
        self.id = id
        self.name = name
        self.dob = dob
        self.__score = {}
    def setScore(self, course_id, score):
        self.__score[course_id] = score
    def getScore(self):
        return self.__score
    def displayInfo(self):
        return f"---------\n{self.id} - {self.name}"

# The Course class 
class Course:
    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name
    def displayInfo(self):
        return f"---------\n{self.id} - {self.name}"
    
class Management:
    # initialize the student and course list
    def __init__(self):
        self.students = []
        self.courses = []

    # enter the student info
    def inputStudentInfo(self):
        studentNum = int(input("Please enter the number of students: "))
        for _ in range(studentNum):
            id = input("Please enter the Student ID: ")
            name = input("Please enter the Student name: ")
            dob = input("Please enter the Student's DOB: ")
            self.students.append(Student(id=id, name = name, dob = dob))

    # enter the course info
    def inputCourseInfo(self):
        courseNum = int(input("Please enter the number of courses: "))
        for _ in range(courseNum):
            id = input("Please enter the Course ID: ")
            name = input("Please enter the Course name: ")
            self.courses.append(Course(id=id, name = name))

    # displaying the overall information
    def displayInfo(self):
        print("\n---Displaying Information---")
        for student in self.students:
            student.displayInfo()
        for course in self.courses:
            course.displayInfo()
    
    # inputing the scores in the list
    def inputScore(self):
        studentID = input("Please enter the Student ID: ")
        courseID = input("Please enter the Course name: ")
        score = int(input(f"Please enter the score for {courseID}"))
        # accessing each elements in students list
        for student in self.students:
            if studentID == student.id:
                student.setScore(courseID, score)

    # displaying all the scores:
    def displayScores(self):
        studentID = input("Enter the Student ID ")
        for student in self.students:
            if student.id == studentID:
                print(f"{student.id}: {student.getScore}")


    # make colors

    def userChoices(self):
        self.inputStudentInfo()
        self.inputCourseInfo()
        while True:
            print("""=================)
                  1. Entering scores 
                  2. Display students and courses information
                  3. Displaying the scores
                  4. Quit
                  =================""")
            choice = input("Choose something...")
            if choice == "1":
                self.inputScore()
            elif choice == "2":
                self.displayInfo()
            elif choice == "3":
                self.displayScores()
            elif choice == "4":
                break
            else:
                print("Invalid choice")

# main
main = Management()
main.userChoices()