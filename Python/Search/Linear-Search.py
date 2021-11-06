
def Linear(R,A):
    x = len(A) # length of array
    i = 0  #  the counter 
    while(i<x):
        if(A[i]==R):
            return i 
        i += 1 
    return -1





# fill the array
size  = int(input("Please entre size of array  : ")) 
B = [0]*size
for i in range(0,size):
    B[i]= i
print(B)
E = int(input("Enter number you want to get index : "))
p = Linear(E,B)
if(p==-1):
    print(f"{E} is not existing in this array !!!! ")
else :
    print(f"The index of {E} is :  {p} ")