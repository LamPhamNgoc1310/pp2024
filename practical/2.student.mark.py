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
    def __init__(self):
        self.id = id