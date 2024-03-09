# The Course class 
class Course:
    def __init__(self, id:str, name:str, weight:float, credits:int):
        self.id = id
        self.name = name
        self.credits = credits
        self.weight = weight
    def displayInfo(self):
        print(f"---------{self.id} - {self.name}---------")