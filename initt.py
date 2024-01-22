class Student:
    def __init__(self,reg_no,name,student_no):
        self.reg_no=reg_no
        self.name=name
        self.student_no=student_no

    def student_details(self):
        print('reg_no,name,student_no',self.reg_no,self.name,self.student_no)

class CS_student(Student):
    course="computer science"
    def student_details(self):
        Student.student_details(self)
        print("course: ",CS_student.course)

student1=Student('23000/49',"Naamusaw",2006)
student1.student_details()
        