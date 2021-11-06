def Binary(R,A,Low,High) :
    x = round((Low+High)/2) # mid of array 
   
    if(R==A[x]):
        return x
    elif  Low >= High : #(Low == x and Low>=High )or (High==x and Low>=High):
        return -1
    elif(R<A[x]):
        High = x-1
        return Binary(R,A,Low,High)
    elif(R>A[x]):
        Low = x+1
        return Binary(R,A,Low,High)




# B = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# fill the array
size  = int(input("Please entre size of array  : ")) 
B = [0]*size
for i in range(0,size):
    B[i]= i
print(B)
E = int(input("Enter number you want to get index : "))
p = Binary(E,B,0,len(B)-1)
if(p==-1):
    print(f"{E} is not existing in this array !!!! ")
else :
    print(f"The index of {E} is :  {p} ")