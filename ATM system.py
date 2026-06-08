print("Balance Check (a)")
print("Withdraw Money (b)")
print("Deposit Money (C)")
bank = {
  1001:{
    "Name":"Deepak",
    "Balance":5000
  },
  1002:{
    "Name":"dipi",
    "Balance":8000
  }
  
}
while True :
  use =  input("enter your operation (Stop): ")
  if use.lower() == "stop":
    break
  if use == "a":
    user = int(input("enter id  : "))
    b=bank[user]["Balance"]
    print("total balance : " ,b)
    
    
  elif use == "b":
    user2 = int(input("enter id  : "))
    uh = int(input(" enter your amount :  : "))
    op = bank[user2]["Balance"]
    ol = op - uh
    print("Withdrawal Successful")
    print("Withdrawn :",uh)
    print("finally balance : ",ol)
    
    
  elif use == "c":
    user4 = int(input("enter id  : "))
    up = int(input(" enter your amount : "))
    lp = bank[user4]["Balance"]
    ui = lp + up
    print("Deposit Successful")
    print("alerd amount :",lp)
    print("Deposited :",up)
    print("finally Balance :",ui)