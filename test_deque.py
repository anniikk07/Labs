from deque import Deque


# __init__

def test_init_size_1():
    d = Deque(1)
    assert d.size == 1
    assert d.count == 0
    assert d.Show() == []


def test_init_size_10():
    d = Deque(10)
    assert d.size == 10
    assert d.count == 0
    assert d.Show() == []


# FillTheDeque

def test_fill_partial():
    d = Deque(10)
    d.FillTheDeque([1, 2, 3, 4])
    assert d.Show() == [1, 2, 3, 4]


def test_fill_full():
    d = Deque(5)
    d.FillTheDeque([10, 20, 30, 40, 50])
    assert d.Show() == [10, 20, 30, 40, 50]


# AddToHead

def test_add_to_head_single():
    d = Deque(5)
    d.AddToHead(7)
    assert d.Show() == [7]


def test_add_to_head_multiple():
    d = Deque(5)
    d.AddToHead(1)
    d.AddToHead(2)
    d.AddToHead(3)
    assert d.Show() == [3, 2, 1]


# AddToTail

def test_add_to_tail_single():
    d = Deque(5)
    d.AddToTail(99)
    assert d.Show() == [67]


def test_add_to_tail_multiple():
    d = Deque(5)
    d.AddToTail(4)
    d.AddToTail(5)
    d.AddToTail(6)
    assert d.Show() == [4, 5, 6]


# DeleteFromHead

def test_delete_from_head_two_elements():
    d = Deque(5)
    d.AddToTail(11)
    d.AddToTail(22)
    assert d.DeleteFromHead() == 11
    assert d.Show() == [22]


def test_delete_from_head_all():
    d = Deque(5)
    d.AddToTail(100)
    d.AddToTail(200)
    assert d.DeleteFromHead() == 100
    assert d.DeleteFromHead() == 200
    assert d.Show() == []


# DeleteFromTail

def test_delete_from_tail_two_elements():
    d = Deque(5)
    d.AddToTail(33)
    d.AddToTail(44)
    assert d.DeleteFromTail() == 44
    assert d.Show() == [33]


def test_delete_from_tail_all():
    d = Deque(5)
    d.AddToTail(300)
    d.AddToTail(400)
    assert d.DeleteFromTail() == 400
    assert d.DeleteFromTail() == 300
    assert d.Show() == []


# GetByIndex

def test_get_by_index_basic():
    d = Deque(5)
    d.AddToTail(10)
    d.AddToTail(20)
    d.AddToTail(30)
    assert d.GetByIndex(0) == 10
    assert d.GetByIndex(2) == 30


def test_get_by_index_after_head_shift():
    d = Deque(5)
    d.AddToTail(5)
    d.AddToTail(6)
    d.AddToTail(7)
    d.DeleteFromHead()          # теперь [6, 7]
    assert d.GetByIndex(0) == 6
    assert d.GetByIndex(1) == 7


# Show

def test_show_empty():
    d = Deque(5)
    assert d.Show() == []


def test_show_after_operations():
    d = Deque(5)
    d.AddToTail(8)
    d.AddToHead(9)
    d.AddToTail(10)
    assert d.Show() == [9, 8, 10]