Sudent = {
  "Dipu":{
    "marks":450,
    "class":"12th",
    "age":"16"
  },
  "deepak":{
    "marks":362,
    "class":"10th",
    "age":"18"
  },
  "liku":{
    "marks":789,
    "class":"9th",
    "age":"78"
  }
}
while True :
  user = input("enter your student name : ")
  if user.lower() == "stop":
   break
  user1 = input("enter your student chack: ")
  if user in Sudent:
    b = Sudent[user][user1]
    print(b)
    user2 = input("enter your student marks: ")
    lo =Sudent[user][user2]
    pt = lo / 600*100
    print("total prsent :",pt)
    
    Sudent[user]["psent"]= pt
   for name, valuse in Sudent.items():
     
     print(name)
      print(valuse["marks"])
      print(valuse["age"])
      print(valuse["class"])
  else:
    print("no student")