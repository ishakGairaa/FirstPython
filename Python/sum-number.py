# sum of number
a=a1 =int(input("Please enter the number do you want to sum = "))
f=0
while(a>0):
  b = a % 10
  f=f+b
  a=int(a//10)
print("The sum of",a1,"is>>>",f)