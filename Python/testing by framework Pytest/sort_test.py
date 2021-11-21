from sort import sort
from random import randint

sort1 = sort()


def test_bubble_sort():
    """ Algorithm  Bubble sort  """

    size = randint(90, 100)
    A = []
    for i in range(0, size):
        A.append(randint(90, 100))
    A = sort1.bubble_sort(A)

    status = True
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            status = False
    assert status, " your method does not work well 'Bubble'  "


def test_selection_sort():
    """ Algorithm  Selection  sort  """

    size = randint(90, 100)
    A = []
    for i in range(0, size):
        A.append(randint(90, 100))
    A = sort1.selection_sort(A)

    status = True
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            status = False
    assert status, " your method does not work well 'Selection'  "


def test_Insertion_sort():
    """ Algorithm  Insertion  sort  """

    size = randint(90, 100)
    A = []
    for i in range(0, size):
        A.append(randint(90, 100))
    A = sort1.Insertion_sort(A)

    status = True
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            status = False
    assert status, " your method does not work well 'Insertion'  "
