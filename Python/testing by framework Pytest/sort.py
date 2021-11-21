class sort:
    from random import randint


    def bubble_sort(self ,B):

        lenB = len(B)
        for  x in range(0,lenB):
            for i in range(0,lenB-x-1):
                if B[i] > B[i+1]:
                    R = B[i+1]
                    B[i+1] = B[i]
                    B[i] = R

        return B


    def selection_sort(self ,B):
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




    def Insertion_sort(self ,B):
        for i in range(0,len(B)-1):
            j = i+1
            R =  B[j]
            while (j>0 and R < B[j-1]):
                B[j] =  B[j-1]
                j-=1
            B[j]=R

        return B


    # size = int(input("Please enter size of array : "))
    # A = []
    # for i in range(0,size):
    #     A.append(randint(-100,100))
    # print(f"Before sorting  =  {A}")
    # # A = Insertion_sort2(A)
    # print(f" After sorting (using 'Insertion sort' ) : {Insertion_sort(A)}")
    # print(f" After sorting (using 'Selection sort' ) : {selection_sort(A)}")
    # print(f" After sorting (using 'Bubble    sort' ) : {bubble_sort(A)}")
