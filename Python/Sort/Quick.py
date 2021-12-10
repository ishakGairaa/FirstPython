
from random import randint



def swap(B,x,y):
    temp = B[x]
    B[x] = B[y]
    B[y]=temp


def midArry(B,start,end):
    mid_index = start
    mid = B[end]
    for i in range(start,end):
        if(B[i]<mid):
            swap(B,i,mid_index)
            mid_index += 1
    swap(B,mid_index,end)
    return mid_index


def Quick_Sort(B,start,end):
    if(start >= end):
        return
    m = midArry(B,start,end)
    Quick_Sort(B,start,m-1)
    Quick_Sort(B,m+1,end)




A =[]
for i in range(0, 10):
    A.append(randint(0,40))


print(A)
Quick_Sort(A,0,len(A)-1)
print(A)
