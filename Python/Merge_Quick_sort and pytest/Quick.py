class Quick:
    from random import randint
    A = []
    start = 0
    end = 0
    def __init__(self,arr,st,en):
        self.A = arr
        self.start = st
        self.end = en
        self.Quick_Sort(self.A,self.start,self.end)


    def swap(self,B,x,y):
        temp = B[x]
        B[x] = B[y]
        B[y]=temp


    def midArry(self,B,start,end):
        mid_index = start
        mid = B[end]
        for i in range(start,end):
            if(B[i]<mid):
                self.swap(B,i,mid_index)
                mid_index += 1
        self.swap(B,mid_index,end)
        return mid_index


    def Quick_Sort(self,B,start,end):
        if(start >= end):
            return
        m = self.midArry(B,start,end)
        self.Quick_Sort(B,start,m-1)
        self.Quick_Sort(B,m+1,end)




    # A =[]
    # for i in range(0, 10):
    #     A.append(randint(0,40))
    #
    #
    # print(A)
    # Quick_Sort(A,0,len(A)-1)
    # print(A)