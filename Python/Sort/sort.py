from random import randint
def bubble_sort(B):
    lenA = len(B)
    lenB = len(B)
    for  x in range(0,lenB):
        for i in range(1,lenA):
            if B[i-1] > B[i]:
                R = B[i]
                B[i] = B[i-1]
                B[i-1] = R
        lenA -= 1
    return B

def bubble_sort2(B):
   
    lenB = len(B)
    for  x in range(0,lenB):
        for i in range(0,lenB-x-1):
            if B[i] > B[i+1]:
                R = B[i+1]
                B[i+1] = B[i]
                B[i] = R

    return B


def selection_sort(B):  
    lenB = len(B)
    for i in range(0,lenB):
        min_index = i
        for j in range(i+1 ,lenB):
            if(B[min_index]>B[j]):
                min_index = j
        if(min_index != i):
            R = B[min_index]
            B[min_index]= B[i]
            B[i]=R
    return B 


def Insertion_sort(B):
    for i in range(0,len(B)-1):
        for j in range(i+1,0,-1):
            if (B[j]< B[j-1]):
                R= B[j]
                B[j]=B[j-1]
                B[j-1]=R
            else :
                break
    return B

def Insertion_sort2(B):
    for i in range(0,len(B)-1):
        j = i+1
        R =  B[j]
        while (j>0 and R < B[j-1]):
            B[j] =  B[j-1]
            j-=1
        B[j]=R

    return B


size = int(input("Please enter size of array : "))
A = []
for i in range(0,size):
    A.append(randint(-100,100))
print(f"Before sorting  =  {A}")
# A = Insertion_sort2(A)
print(f" After sorting (using 'Insertion sort' ) : {Insertion_sort2(A)}")
print(f" After sorting (using 'Selection sort' ) : {selection_sort(A)}")
print(f" After sorting (using 'Bubble    sort' ) : {bubble_sort2(A)}")
