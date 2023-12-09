from Student import Student

def writetofile(slist):
    with open("students.txt","w") as file1:
        for rec in slist:
            file1.write(str(
rec.id
)+" "+rec.name+" "+rec.surname+"\n")
        file1.close()


studentslist = []
newStudent = Student(0,"John","Doe")
studentslist.append(newStudent)
studentslist.append(Student(1,"Jane","Doe"))
writetofile(studentslist) 