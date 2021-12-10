from Quick import Quick
from random import randint


def test_Quick():
    """ Algorithm of   Quick sort  """
    size = randint(10, 10)
    A = []
    for i in range(0, size):
        A.append(randint(0, 100))
    print(A)
    d = size-1
    Quick1 = Quick(A,0,d)
    print(A)
    status = True
    for i in range(0,d):
        if A[i] > A[i + 1]:
            status = False
    assert status, " your method does not work well 'Quick'  "


