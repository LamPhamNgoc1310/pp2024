class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.__score = {}
    def setScore(self, course_id, score):
        self.__score[course_id] = score
    def getScore(self):
        return self.__score
    def displayInfo(self):
        print(f"Student ID: {self.id}\nStudent name: {self.name}\nDOB: {self.dob}")
