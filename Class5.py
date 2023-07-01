class Person:
    PID = None
    PName = None
    PGender = None
    PCity = None
    PDOB = None
    def _init_(obj,idd,name,gender,city,dob):
        obj.PID = idd
        obj.PName = name
        obj.PGender = gender
        obj.PCity = city
        obj.PDOB = dob

    def calcAge(obj):
        return 2023 - int(obj.PDOB[0:4])

class Student(Person):
    SID = None
    SMarks = None
    SAge = None
    def _init_(obj,idd,name,gender,city,dob,sid,marks):
        obj.PID = idd
        obj.PName = name
        obj.PGender = gender
        obj.PCity = city
        obj.PDOB = dob
        obj.SAge = obj.calcAge()
        obj.SID = sid
        obj.SMarks = marks
    def printStudent(obj):
        print("Student Details")
        print("Person ID= ",obj.PID,"Student ID =",obj.SID)
        print("Student Name =",obj.PName)
        print("Student Gender=",obj.PGender)
        print("Student City=",obj.PCity)
        print("DOB =",obj.PDOB,"Age =",obj.SAge)
        print("Marks=",obj.SMarks)

s1 = Student(12345,"Priya","F","Chennai","1985/09/23","SIT12",eval("[100,90,95,99,100]"))
s1.printStudent()
