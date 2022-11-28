from Student import Student
from SchoolClass import SchoolClass
from School import School

std1 = Student("Mikri","Annoula","Totos","1234454321",[10,10,10])
a1 = SchoolClass("A1",[std1],25)
mega = School("Mega",[a1])

def searchProblems(school):
    for cl in school.schoolclasslist:
        if a1.hasProblem():
            print("overloaded") 

print(mega.classrooms[0].studentsList[0].grades) 