class Course:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        # self.studentNumber = studentNumber
    def displayInfo(self):
        print(f" -------------- \nCourse ID: {self.__id} \nCourse Name: {self.name}")