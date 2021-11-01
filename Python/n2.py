# does the array have duplicate ? 
import random
def hasDuplicate(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if(i==j):
               continue
            if (A[i]==A[j]):
                 return True,A[i]
    return False


A = [0]*10
for i in  range(0,10):
    A[i] = random.randrange(50)
print(A)

print(f"{hasDuplicate(A)}")