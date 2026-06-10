user = int(input("how many data add"))
username = "lopp"
password= 890
data = []
for i in range(user):
  lp = input("Enter username :")
  ll = int(input("Enter password :"))
  data.append(lp)
  data.append(ll)
  if username and password in data :
    print("Login Successful :",lp)
    break
  else :
    print("no")
  