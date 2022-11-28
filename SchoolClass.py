from Student import Student

class SchoolClass:
    def __init__(self,name,studentsList,capacity) -> None:
        self.name = name
        self.capacity = capacity
        self.studentsList = studentsList
    def hasProblem(self):
        if self.capacity < len(self.studentsList):
            return True
        else:
            return False

    def hasStudent(self,searchSurname):
        resultList = []
        for std in self.studentsList:
            if std.name == searchSurname:
                resultList.append(std)
        return resultList