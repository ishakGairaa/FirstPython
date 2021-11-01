# number Fibonacci
a =int(input("Enter the number = "))
n=0
n1=1
c=a
for i in range(1,abs(a)):
  c=n+n1
  n=n1
  n1=c
if(a<0):
  c=abs(c)*pow(-1,a+1)
print("Fibonacci of",a,"is = ",int(c))