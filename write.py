students_data = []

while True:
    registration_number = input("Enter Registration Number: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    student_info = {
        "RegistrationNumber": registration_number,
        "Name": name,
        "Age": age
    }

    students_data.append(student_info)

    print("\nStudents' Bio-Data:")
    for student in students_data:
        print(f"Registration Number: {student['RegistrationNumber']}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print("-" * 20)

    continue_integer=int(input("Enter 1 to CONTINUE or any other number to STOP\n"))
    if continue_integer!=1:
        break
