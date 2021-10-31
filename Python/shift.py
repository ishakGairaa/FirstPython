import random 
# using  variable   
def var01(A,x):
    y= 0
    for g in range(0,x):
        y = A[-1]
        for j in range(2,len(A)+1):
            A[-j+1] = A[-j]
        A[0] = y
    return print(A)  
 
# using another Array 
def var02(A ,x):
    B = [0]*len(A)
    y=x 
    r=0
    for j in range(0,x):
        B[j] = A[len(A)-y]
        y -= 1 
    for g in range(x,len(A)):
        B[g] = A[r]
        r += 1
    print(B)

# using another  length of shift equal  length of array 
def var03(A ,x):
    p = len(A)
    B = [0]*x
    t = 0
    for j in range(p-x,p):
        B[t] = A[j]
        t +=1
    for g in range(p-1-x,-1,-1):
        A[g+x] = A[g]
    for i in range(0,x):
        A[i]=B[i]
    print(A)
    print(B)

w = int(input("Enter the length of your array = ")) 
B = [0]*w
# fill in  the array with random numbers 
for i in  range(0,w):
    B[i] = random.randrange(50) 

print(f" First Array  = {B}")
x = int(input("Enter the number you want to shift the array =  "))
#var02(B,x)
var03(B,x)
#var01(B,x)