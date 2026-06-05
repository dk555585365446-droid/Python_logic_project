print("Search Marks (1)")
print("Add New Student(2)")
student = {
  "Deepak":"85",
  "dipu":"78",
  "Rocky": "56"
  
}

for i in student.keys():
  print(i)
  
user2  = input("enter your operation  : ")
if user2 == "1" :
  user = input("enter your name : ")
  if user in student :
    print("areld add")
    b = student[user]
    print("mark : ",b)
  else :
    print("name is not found")

elif user2 == "2" :
  user3 = input("enter your key : ")
  user4 = input("enter your value : ")
  student[user3] = user4
  print("Student Added Successfully")
  for key, value in student.items():
    print(key, ":",value)
