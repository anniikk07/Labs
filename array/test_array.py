from myarray import Array

def test_init_():
    my_arr = Array([1, 2, 3])
    assert my_arr == [1, 2, 3]

def test_add_to_tail():
    my_arr = Array([1, 2, 3])
    my_arr.add_to_tail(4)
    assert my_arr == [1, 2, 3, 4]

def test_add_by_index():
    my_arr = Array([1, 2, 3])
    my_arr.add_by_index(0, 0)
    assert my_arr == [0, 1, 2, 3]

def test_remove_by_index():
    my_arr = Array([1, 2, 3])
    my_arr.remove_by_index(0)
    assert my_arr == [2, 3]

def test_find_by_index():
    my_arr = Array([1, 2, 3])
    ans = my_arr.find_by_index(0)
    assert ans == 1

def test_find_by_value():
    my_arr = Array([1, 2, 3])
    ans = my_arr.find_by_value(2)
    n = my_arr.find_by_value(0)
    assert ans == 1
    assert n == 'Ничего не найдено'
