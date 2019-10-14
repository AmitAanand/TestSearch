

class Company:
    company_name="Inventatech"
    company_city="Bangalore"

    def __init__(self,emp_id,name,salary,location):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.location=location

    def emp_info(self):
        print(self.emp_id)
        print(self.name)

    @classmethod
    def comp_adress(cls):
        print(cls.company_name)
        print(cls.company_city)


comp1=Company('E001','Bahubali',50000,'BTM')
comp1.emp_info()
comp1.comp_adress()

comp2=Company('E002','Thangabali',80000,'Marthalli')
comp2.emp_info()
comp2.comp_adress()

comp3=Company('E003','Bhanumathi',60000,'Jayanagar')
comp3.emp_info()
comp3.comp_adress()
