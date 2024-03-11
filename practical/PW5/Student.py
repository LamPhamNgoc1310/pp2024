
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
        print(f"---------{self.id} - {self.name} - {self.dob}---------")
    def calGPA(self, creditsDict, weightDict):
        totalScore = 0
        totalCred = 0
        for course_id, score in self.__score.items():
            if course_id in creditsDict:
                totalScore += score * weightDict[course_id]*creditsDict[course_id]
                totalCred += creditsDict[course_id]
        if totalCred > 0:
            self.gpa = totalScore / totalCred
        else:
            print("The information for the student is incomplete or incorrect.")
        return self.gpa
