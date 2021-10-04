# factorial of num
x =abs(int(input("Enter the number = ")))
a=1
for i in range(0,x):
  a=a*(x-i)
print("the factorial of",x,"! is >>>",a)