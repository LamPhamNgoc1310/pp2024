import Student
import Course

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
        courses[code] = Course(code, name)

print("-------Score insertion-------")

id = int(input("Student ID: "))
course_code = input("Course ID: ")
score = int(input("Score: "))
for student in students:
    if student.id == id:
        student.setScore(course_code, score)


for student in students:
    student.displayInfo()

for course in courses.values():
    course.displayInfo()

# id = int(input("Student ID: "))
# for student in students:
#     if student.id == id:
#         print(f"Student {student.id} scored {student.score}")
    
id = int(input("Student ID: "))
for student in students:
    if student.id == id:
        print(f"Scores: {student.getScore()}")