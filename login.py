user = {
  "Deepak":"1234",
  "dipu" : "4567",
  "liku" : "90876"
}
name = input("enter your name : ")
password = input("enter your password : ")
if name in user :
  if user[name] in password :
    print("login seussful")
    print("wellcom :",name)
    
  else :
    print("invalid password")
    print("login falie ")

else :
  print("name not found")
  print("login fali")
