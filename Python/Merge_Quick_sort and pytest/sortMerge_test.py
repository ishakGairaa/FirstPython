from Merge import Merge
from random import randint




def test_Merge():
    """ Algorithm of   Merge sort  """
    size = randint(10, 10)
    A = []
    for i in range(0, size):
        A.append(randint(0, 100))
    print(A)
    d = size-1
    Merge1 = Merge(A)
    print(A)
    status = True
    for i in range(0,d):
        if A[i] > A[i + 1]:
            status = False
    assert status, " your method does not work well 'Merge'  "

