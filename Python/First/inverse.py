#inverse number 
a=a1 =int(input("Enter the number you want to inverse = "))
f=0
while(a>0):
  b = a % 10
  f=f*10+b
  a=int(a//10)
print("inverse of",a1,"is >>>>",int(f))



