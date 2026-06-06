# sharch mark
print("search for student(a)")
print("add a student(b)")
print("Add Existing Student (c)")
student ={
  "Deepak": 362,
  "dipu": 450,
  "liku":456,
  "siku":234
}
# student search
io = input("enter your opertion : ")
if io == "a":
  user = input("enter your name :")
  if user in student :
    print("Student Found")
    print(user, ":",student[user])
  else :
    print(" student not Found ")
# student add 
elif io == "b":
  user1 = input("enter your name :")
  user2 = int(input("enter your mark :"))
  student[user1] = user2
  print("Student Added \n Successfully")
  for key, value in student.items():
    print(key, ":",value)
# student Deleted
elif io == "c":
  user3 = input("enter your name :")
  if user3 in student :
    del student[user3]
    print("Deleted Successfully")
    for key, value in student.items():
      print(key, ":",value)
  else :
    print("student not found")
  
  
  
  