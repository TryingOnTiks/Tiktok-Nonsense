students = []
student_id = 1
def add_student():
    global student_id
    print("\n=====ADD STUDENT====")
    student_name = input("Enter student name: ")

    student = {
         "id": student_id,
         "name": student_name,
         "grades": {}
    }
    students.append(student)

    student_id += 1
    
def add_grade():
       found = False
       
       print("\n====ADD STUDENT GRADE====")
       select_id = int(input("Enter student ID: "))

       for student in students:
            if select_id == student["id"]:
                 print(f"Name: {student['name']}")
                 found = True
                 english = int(input("Input Grade in English: "))
                 math = int(input("Input Grade in Math: "))
                 science = int(input("Input Grade in Science: "))

                 student["grades"] = {
                      "english": english,
                      "math": math,
                      "science": science
                 }
                 break
            
       if not found:
            print("User Not Found.")

def view_students():
       print("\n======ALL STUDENTS====")
       for student in students:
            print(f"{student['id']} - {student['name']}")

def view_student_grade():
       found = False
       
       print("\n======ALL STUDENTS====")
       for student in students:
            print(f"{student['id']} - {student['name']}")

       select_id = int(input("Enter Student ID: "))

    
       for student in students:
        if select_id == student["id"]:
                found = True

                if not student["grades"]:
                     print("No grade yet")
                     return
                
                print(f"\n=====Student Grade=====")
                print(f"Name: {student['name']}")
                print(f"English: {student['grades']['english']}")
                print(f"Math: {student['grades']['math']}")
                print(f"Science: {student['grades']['science']}")
                break
        
       if not found:
            print("Student ID NOT Found.")
def calculate_average():
     found = False
     
     print("\n======ALL STUDENTS====")
     for student in students:
          print(f"{student['id']} - {student['name']}")

     select_id  = int(input("Enter Student ID: "))

     for student in students:
          if select_id == student["id"]:
               found = True
               print(f"\n======STUDENT AVERAGE======")
               print(f"Name: {student['name']}")
               print(f"English: {student['grades']['english']}")
               print(f"Math: {student['grades']['math']}")
               print(f"Science: {student['grades']['science']}")

               total = (student['grades']['english'] + 
                        student['grades']['math'] + 
                        student['grades']['science'])
               
               average = total / 3

               print(f"Total: {total}")
               print(f"Average: {average}")

     if not found:
        print("Student ID Not Found.")     

while True:
    print("\n===Student Record System===")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Students")
    print("4. View Student Grade")
    print("5. Calculate Average")
    print("6. Exit")

    user_input = input("Enter Option(1-6): ")

    if user_input == "1":
        add_student()
    elif user_input == "2":
        add_grade()
    elif user_input == "3":
        view_students()
    elif user_input == "4":
        view_student_grade()
    elif user_input == "5":
        calculate_average()
    elif user_input == "6":
           print("Exit.")
           break
    else:
         print("Invalid input")