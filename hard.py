class Basic_Calculator:
    # add
    def add (x,y):
        return x+y
    # sub
    def subtract (x,y):
        return x-y
    # multiply
    def multiply (x,y):
        return x*y
    # divide
    def divide (x,y):
        if y!=0:
            return x+y
        else:
            print("Cannot divide by 0")

class Student_Numbers(Basic_Calculator):
    def Total_Marks(self):
        total1=0
        student_number_list=[2300700459,2300724122,2300710315,2200705152]
        for number in student_number_list:
            total1+=number
        print("the total of the student numbers is\n",total1)

        total2=str(total1)
        CU1,CU2,CU3,CU4=None,None,None,None
        # print(len(total2))

        for i in range(2,len(total2),2):
            if i==2:
                CU1=int(total2[i:i+2])
            elif i==4:
                CU2=int(total2[i:i+2])
            elif i==6:
                CU3=int(total2[i:i+2])

            elif i==8:
                CU4=int(total2[i:i+2])

        return CU1,CU2,CU3,CU4
        
    def grade_points(self,mark_list):
        results=[]
        for marks in mark_list:
            if 90<=marks<=100:
                results.append((marks,5.0))
            elif 80<=marks<=89:
                results.append((marks,5.0))
            elif 75<=marks<=79:
                results.append((marks,4.5))
            elif 70<=marks<=74:
                results.append((marks,4.0))
            elif 65<=marks<=69:
                results.append((marks,3.5))
            elif 60<=marks<=64:
                results.append((marks,3.0))
            elif 55<=marks<=59:
                results.append((marks,2.5))
            elif 50<=marks<=54:
                results.append((marks,2.0))
            elif 45<=marks<=49:
                results.append((marks,1.5))
            elif 40<=marks<=44:
                results.append((marks,1.0))
            elif 0<=marks<=40:
                results.append((marks,0.0))
        return results
    
class CGPA(Basic_Calculator):
    def calculate_cgpa(self,marks_obtained):
        total_credit_points=0
        total_credits=0
        for credits, grade in marks_obtained:
            credit_points=Basic_Calculator.multiply(credits,grade)
            total_credit_points=Basic_Calculator.add(total_credit_points,credit_points)
            total_credits=Basic_Calculator.add(total_credits,credits)
        gpa=Basic_Calculator.divide(total_credit_points,total_credits)
        return gpa


student=Student_Numbers()
CU1,CU2,CU3,CU4=student.Total_Marks()
results=student.grade_points([CU1,CU2,CU3,CU4])
marks_obtained=results
print("the list for your results is:\n",results)

cgpa2=CGPA().calculate_cgpa(marks_obtained)
print("the cgpa is\n", cgpa2)
            

