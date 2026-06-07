print("Add Multiple Expenses(a)")
print("Category Wise Trackinkg(b)")

io = input("enter your operation : ")
if io == "a" :
  user = int(input("how many expansive "))
  data = {}
  for i in range(user):
    a = input("Enter expense name : ")
    b = input("Enter category : ")
    c = int(input("Enter amount : "))
    data[a] = {
      "category" : a,
      "amount" : c
    
  }

  for key, info in data.items():
    print( a, ":", info["amount"])
  print("Records Saved Successfully")
  with open("Deepak.txt", "a") as file :
    file.write(b)
    file.write(":" +  str(c)  + "\n") 
    file.close()
elif io == "b":
  with open("Deepak.txt", "a") as fil :
    bn = fil.read()
    print(bn)

