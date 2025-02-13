#student record mamagement system
student={} #student data
studentId=[]#list to trak studentId

while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Search Student")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        id = int(input("Enter Student Id: "))
        if id in studentId:
            print("Student id already present in database")
        else:
            name = input("Enter Student Name: ")
            age = int(input("Enter student age: "))
            marks = int(input("Enter student marks: "))
            studentId.append(id)
            student[id] = {"name": name, "age": age, "marks": marks}
            print("Student Added Successfully")

    elif choice == 2:
        print(studentId)
        print(student)
    
    elif choice == 3:
        id=int(input("Enter Student Id: "))
        del student[id]
        studentId.remove(id)
        print("Student Data is deleted Sucessfully")
    
    elif choice==4:
        id=int(input("Enter Student Id to Update"))
        if id in student:
            name=input("Enter Student Name to Update:")
            marks=int(input("Enter Student Marks to Update:"))
            age=int(input("Enter Student Age to Update:"))
            student[id]={"name":name,"age":age,"marks":marks}
            print("Student Data is Updated Sucessfully")
        else:
            print("Student Id not found")
    
    elif choice==5:
        id=int(input("Enter student Id to serach"))
        if id in student:
            print("Student Id\tStudent Name\tStudent Age\tStudent Marks")
            print(id, "\t", student[id]["name"], "\t", student[id]["age"], "\t", student[id]["marks"])
        else:
            print("Student Id not found")
   
    elif choice == 6:
        break
    else:
        print("Invalid Choice")