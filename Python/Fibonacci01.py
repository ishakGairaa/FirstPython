# number Fibonacci 
def Fob(a):
    if(a==0):
        return 0
    elif(a==1):
        return 1
    elif(f[a]>0):
        return f[a]
    f[a]=Fob(a-1)+Fob(a-2)
    return f[a]
a1 =int(input("Enter the number = "))
a=abs(a1)
f=[0]*(a+1)
s=Fob(a)
if(a1<0):
    s=Fob(a)*pow(-1,a1+1)
else:
    s=Fob(a)
print("Fibonacci of",a1,"is = ",int(s))