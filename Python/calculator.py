#calculator 
a = float(input("Please enter the first variable A = "))
b = float(input("Please enter the second variable B = "))
a1 = int(input(
        "tap 1 if you want '+' =\ntap 2 if you want '-' =\ntap 3 if you want '*'=\ntap 4 if you want '/'= "
    ))
if(a1==1):
  a = int(a+b)
  print(a)
elif(a1==2):
  a=int(a-b)
  print(a)
elif(a1==3):
  a=a*b
  print(a)
elif(a1==4):
  if(b!=0):
      a=a/b
      print(a)
  else:
     print("you can't divide on zero !!!!!! ")
else:
  print("the number is not 1.2.3.4")