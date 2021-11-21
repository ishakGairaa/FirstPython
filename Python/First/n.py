#complexity O(n) 
# fill the array 
import random
F = [0]*10
for i in  range(0,10):
    F[i] = random.randrange(50)
print(F)
# searching in array for  maximun value 
x=F[0]
for i in range(1,len(F)):
    if(x<F[i]):
        x=F[i]
print(f"maximun in array  is = {x} ")