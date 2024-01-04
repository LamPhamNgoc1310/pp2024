student = []
course = {}

def studentNumber():
    s = int(input("Number of student: "))
    # print(f"Total number of students: {n}")
    #return the number of students to main
    return s
    
def studentInfo(studentNumber):
    for _ in range(studentNumber):
        id = int(input("Student ID: "))
        name = input("Student Name: ")
        DoB = input("DoB: ")
        student.append(id, name, DoB, {})

def courseNumber():
    c = int(input("Number of courses: "))
    #return the number of students to main
    return c 

def courseInfo(courseNumber):
    for _ in range(courseNumber):
        id = int(input("Course ID: "))
        name = input("Course Name: ")
    
def setScore():
    c = input("Select your course: ")


# def dispStudents():
# def dispCourses():
# def dispScore():
s = studentNumber()
studentInfo(s)
c = courseNumber()
courseInfo(c)

