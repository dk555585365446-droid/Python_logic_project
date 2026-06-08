# Bim calculater
user = int(input("enter your wegiht : "))
user1 = int(input("enter your hight : "))
b = user1 / 100
kl = b*b
bim = user / kl
print(bim)
if  bim <= 18.5 :
  print("Underweight")
elif bim <= 24.9 :
  print("Normal Weight")
elif bim <= 29.9 :
  print("Overweight")
elif bim >= 30 :
  print("Obesity")