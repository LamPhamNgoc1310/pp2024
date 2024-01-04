# Students in a list 
students = []
# Course in a dictionary
course = {}

#Entering students Info
def studentNumber():
    print("-------Student Infomation-------")
    s = int(input("Number of student: "))
    #return the number of students to main
    return s
    
def studentInfo(studentNumber):
    for _ in range(studentNumber):
        print("----Student----")
        id = int(input("Student ID: "))
        name = input("Student Name: ")
        DoB = input("DoB: ")
        students.append((id, name, DoB, {}))

#Entering courses information
def courseNumber():
    print("-------Course Information-------")
    c = int(input("Number of courses: "))
    #return the number of students to main
    return c 


def courseInfo(courseNumber):
    for _ in range(courseNumber):
        id = int(input("Course ID: "))
        name = input("Course Name: ")
        course[id] = name
    
def setScore():
    print("-------Score insertion-------")

    id = int(input("Student ID: "))
    course_id = int(input("Course ID: "))
    score = int(input("Score: "))
    for student in students:
        if student[0] == id:
            student[3][course_id] = score

#display Students list
def dispStudents():
    print("-----Student Information Display-----")
    for student in students:
        print(f"Student ID: {student[0]} | Student Name: {student[1]} | DoB: {student[2]}")

#display Courses dictionary
def dispCourses():
    print("-----Course Information Display-----")
    for course_id, name in course.items():
        print(f"Course ID: {course_id} | Name: {name}")

#display Score list
def dispScore(course_id):
    print("-----Score Information Display-----")
    for student in students:
        if course_id == student[3]:
            print(f"Student ID: {student[0]} | Score: {student[3][course_id]}")

s = studentNumber()
studentInfo(s)

c = courseNumber()
courseInfo(c)
setScore()

dispStudents()
dispCourses()

n = input("Course ID?")
dispScore(n)

