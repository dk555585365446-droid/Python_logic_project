# user enter your story
while True :
  name = input("enter your story (stop ): ")
  if name.lower() == "stop":
    break
  b = name.title()
  print(b)
