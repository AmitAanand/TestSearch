import datetime
from datetime import datetime

class Student:
    fees=20000
    student_count=0
    def __init__(self,name,age,course):
        Student.student_count+=1
        self.roll_no=Student.student_count
        self.name=name
        self.age=age
        self.course=course

    def print_info(self):
        print("Roll_No :",self.roll_no)
        print(self.name)
        print(self.age)
        print(self.course)

    @classmethod
    def discount(cls,dis):
        return  Student.fees- dis/100*cls.fees

    @staticmethod
    def validate_dob(dob):
        doj=datetime.strptime(dob,"%d/%m/%Y")
        present_date=datetime.now()
        print(present_date,doj)



obj1=Student('Raj',25,'Python')
obj1.print_info()
print("Discounted Fee :",Student.discount(20))
print("Count of Student :",Student.student_count)

print(Student.validate_dob('28/07/2018'))

obj2=Student('sid',20,'Java')
obj2.print_info()
print("Discounted Fee :",Student.discount(20))
print("Count of Student :",Student.student_count)