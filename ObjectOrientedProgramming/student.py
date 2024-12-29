class Student:
    name:str
    rollnumber:int
    age:int
    course:str


    def set_student(self,name,rollnumber,age,course):
        self.name=name
        self.rollnumber=rollnumber
        self.age=age
        self.course=course


    def display(self):
        print(self.name,self.rollnumber,self.age,self.course)    


student_instance1=Student()
student_instance2=Student()

student_instance1.set_student("Alan",11,23,"python")
student_instance2.set_student("John",20,22,"java")

student_instance1.display()