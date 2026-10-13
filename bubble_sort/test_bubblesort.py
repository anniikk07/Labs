from bubblesort import bubble_sort

def test_1():
    arr = [1, 4, 3, 2, 5]
    ans = bubble_sort(arr)
    assert ans == [1, 2, 3, 4, 5]

def test_2():
    arr = [4, 5, 5, 23, 12, 24, 27, 19, 0, 23]
    ans = bubble_sort(arr)
    assert ans == [0, 4, 5, 5, 12, 19, 23, 23, 24, 27]
