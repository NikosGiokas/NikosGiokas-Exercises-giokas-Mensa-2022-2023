####
# 
#Askiseis class v2
#Askisi 3
# 
#   @author Niko
#  Version  0.0.2
#  Date  15.12.2022    
#    
# #
studentCount = 0
class Student:
    global studentCount
    def __init__(self, name, grades):
        global studentCount
        self.name=name
        self.grades=grades
        studentCount += 1

    def sayHello(self,name):
        self.name = name
        print("hello",self.name)
    def averageGrades(self,grades):
        self.grades = grades
        avg = 0
        for grade in grades:
            avg  += grade
        print(round(avg/len(grades),2))
        return round(avg/len(grades),2)


niko = Student("Niko",[16,18,17,15,15,20,20])
benjamin = Student("benjamin",[16,18,17,15,15,20,20])
rayk = Student("rayk",[15,18,17,15,15,15,20])
yohann = Student("yohann",[16,18,17,20,20,20,20])
jonah = Student("jonah",[16,18,17,15,15,20,20])
students = [niko,benjamin,rayk,yohann,jonah]




for student in students:
    if ( student.averageGrades(student.grades) >= 18 ):
        print("O ", student.name ,"has an average of 18 or more")

def bestStudent():
    best = 0
    for student in students:
        if student.averageGrades(student.grades) > best:
            best = student.averageGrades(student.grades)
            name = student.name
    print(name,"is the best") 
        
bestStudent()