n=input("Enter the number of students : ")
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks[:]
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Marks in 3 subjects : ",marks)
marks=[]
def accept(n):
    name=input("Student {} : ".format(n))
    age=input("Age : ")
    for m in range(3):
        marks.append((input("Score in subject {} : ".format(m+1))))
    return name,age,marks

for i in [1,n]:
    name,age,marks=accept(i)
    student=Student(name,age,marks)

for i in [1,n]:
    student.display()
