# shop mangment
shop ={
  "pizza":120,
  "coffe": 80,
  "tea":50,
  "bsaket": 30,
  "pasta" : 60
}
for key, value in shop.items():
  print(key, ":",value)
print("\nwellcom for diamen")
user = input("enter your oder : ")
print("your oder susseful ")
b = shop[user]
use1 =  input("are your oder (yes / no )")
if use1 == "yes":
  use2 = input("enter your oder : ")
  v = shop[use2]
  gh = b + v
  print("finally bill : ",gh)

else :
  print("ok no thanks ")
  print("finally bill : ",b)
  