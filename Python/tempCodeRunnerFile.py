
def Binary(R,A,Low,High) :
    x = round((Low+High)/2)
    print(f"  x = {x}     Low =   {Low}      High =   {High}  ")
    if(R==A[x]):
        print(f" the result is {x} ")
        return x
    elif(R<A[x]):
        High = x-1
        print(f"              {A[Low:High+1]}")
        return Binary(R,A,Low,High)
    elif(R>A[x]):
        Low = x+1
        print(f"             {A[Low:High+1]}")
        return Binary(R,A,Low,High)
    elif(Low+1==High):
        return -1




B = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print(B)
p = Binary(int(input("Enter number you want to get index : ")),B,0,len(B)-1)
print(f"             :    :   : {p} ")