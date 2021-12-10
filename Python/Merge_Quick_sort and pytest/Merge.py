class Merge:

    from random import randint
    A = []
    def __init__(self,arr):
        self.A = arr
        self.Merge_Sort(self.A)

    def Merge_Sort(self,Array):
        if len(Array) > 1:
            mid = len(Array) // 2
            left = Array[:mid]
            right = Array[mid:]
            self.Merge_Sort(left)
            self.Merge_Sort(right)
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    Array[k] = left[i]
                    i += 1
                else:
                    Array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                Array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                Array[k] = right[j]
                j += 1
                k += 1


    # B = []
    # for i in range(0, 10):
    #     B.append(randint(0, 40))
    #
    # print(f"{B}")
    # Merge_Sort(B)
    #
    # print(B)
