# This is Program of Adding students Records
records = [] 

def Add_Students():
   dict_records = {
    "Name": input("Enter Student Name: "), 
    "Roll_no": input("Enter Student Roll Number: "),
    "Subject": input("Enter Student Subject: "),
    "Marks": int(input("Enter Student Marks: "))
   }

   records.append(dict_records)
print("Details Successfully added")


def Display_Student():
   if not records:
       print("No Records Found!") 
   else: 
       for dict_records in records:
           print(dict_records)


def Search_Student():
 roll_num = input("Enter roll number to find student:  ")
 for dict_records in records:
    if dict_records["Roll_no"] == roll_num:
        print("--------------")
        print("Student Found!", dict_records)
        return dict_records, records.index(dict_records)
        print("--------------") 
        
    else:
        print("Student not Found")
        return None, None
  


# Update Student Marks

def Update_Student():
    dict_records, index = Search_Student()

    if dict_records is not None:

        print("Records Found!")
        
        print("Current Marks:", dict_records['Marks'])
        


    #  getting marks for update
        update_marks = int(input("Enter marks to update:"))
    # updating marks
        dict_records['Marks'] = update_marks
        records[index] = dict_records
        print("Student Record updated Successfully!") 
    else:
        print("No Student Found!") 
   

#  Deleting the record of a student
def Delete_Record():
  dict_records, _ = Search_Student()
  if dict_records is not None:
    records.remove(dict_records) 
    print("Record Deleted Successfully!")
  else:
    print("Record not Found! Unable to delete")

 # Sort Student Data
def Sort_Student_Record():
   if not records:
       print("Sorry! No Records Found!")
       return 

   # Sort records by marks (descending)
   else:
       records.sort(key=lambda x: x['Marks'], reverse=True)
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


# The program ends here