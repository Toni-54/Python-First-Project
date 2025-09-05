# Program to manage student records using nested lists
records = [] 

def Add_Students():
    name = input("Enter student  name: ")
    roll_num = input("Enter student roll number: ")
    subject = input("Enter student subject: ")
    marks = int(input("Enter students marks: "))
    
    records.append([name,roll_num,subject,marks])
    print("Details Successfully added")
   


def Display_Student():
 if records is None:
  print("No Records Found!") 
 else: 
  for student in records:
   print(".........................................................")
   print("Student Records!")
   
  
   print(f"Name:{student[0]}")
   print(f"Roll Number:{student[1]}")
   print(f"Subject:{student[2]}")
   print(f"Marks:{student[3]}")
   print("-------------------------------------------------------")
 
    


def Search_Student():
 roll_num = input("Enter roll number to find student:  ")
 for  student in records:
  if student[1] == roll_num:
   print("--------------")
   print("Student Found!") 
  
   print(f"Name:{student[0]}")
   print(f"Roll Nunber:{student[1]}")
   print(f"Subject:{student[2]}")
   print(f"Marks:{student[3]}")
   return student, records.index(student)
  else:
    print("Student not Found")
    return None, None

# Update Student Marks

def Update_Student():
    student, index = Search_Student()
   
    if student is not None:
        
        print("Records Found!")
        
        print(f"Name: {student[0]}")
        print(f"Roll Nunber: {student[1]}")
        print(f"Subject: {student[2]}")
        print(f"Marks: {student[3]}")

    #  getting marks for update
        update_marks = int(input("Enter marks to update:"))
    # updating marks
        student[3] = update_marks
        records[index] = student
        print("Student Record updated Successfully!") 
    else:
        print("No Student Found!")
   

#  Deleting the record of a student
def Delete_Record():
  student_found, _ = Search_Student()
  if student_found is not None:
    records.remove(student_found) 
    print("Record Deleted Successfully!")
  else:
    print("Record not Found! Unable to delete")

 # Sort Student Data
def Sort_Student_Record():
   if not records:
       print("No records to sort.")
       return 

   # Sort records by marks (descending)
   records.sort(key=lambda x: x[3], reverse=True)
   print("Records sorted by marks (highest to lowest).")

while True:
 print("1, Add Student")
 print("2, Display Student ")
 print("3, Search Student ")
 print("4, Update Student")
 print("5, Delete Student")
 print("6, Sort Student ")
 print("7, Exit")

 user_choice = int(input("Enter your choice: "))

 if user_choice == 1:
  Add_Students()
 elif user_choice == 2:
  Display_Student()
 elif user_choice == 3:
  Search_Student()
 elif user_choice == 4:
  Update_Student()
 elif user_choice == 5:
  Delete_Record()
 elif user_choice == 6:
  Sort_Student_Record()
 elif user_choice == 7:
  break 
 else:
  print("You have chosen a invalid choice! ")


#   This Program ends here 
