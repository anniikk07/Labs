from mylist import List

def test_add_to_head():
    my_list = List()
    my_list.add_to_head(1)
    my_list.add_to_head(2)
    my_list.add_to_head(3)
    assert str(my_list) == '3 <-> 2 <-> 1'

def test_add_to_tail():
    my_list = List()
    my_list.add_to_tail(1)
    my_list.add_to_tail(2)
    my_list.add_to_tail(3)
    assert str(my_list) == '1 <-> 2 <-> 3'


def test_add_by_index():
    my_list = List()
    my_list.add_to_tail(1)
    my_list.add_to_tail(3)
    my_list.add_by_index(2, 1)
    assert str(my_list) == '1 <-> 2 <-> 3'


def test_remove_from_head():
    my_list = List()
    my_list.add_to_tail(1)
    my_list.add_to_tail(2)
    my_list.remove_from_head()
    assert str(my_list) == '2'


def test_remove_from_tail():
    my_list = List()
    my_list.add_to_tail(1)
    my_list.add_to_tail(2)
    my_list.remove_from_tail()
    assert str(my_list) == '1'


def test_remove_by_index():
    my_list = List()
    my_list.add_to_tail(1)
    my_list.add_to_tail(2)
    my_list.add_to_tail(3)
    my_list.remove_by_index(1)
    assert str(my_list) == '1 <-> 3'


def test_find_by_value():
    my_list = List()
    my_list.add_to_tail(10)
    my_list.add_to_tail(20)
    ans = my_list.find_by_value(20)
    assert ans == 1


def test_find_by_index():
    my_list = List()
    my_list.add_to_tail(10)
    my_list.add_to_tail(20)
    node = my_list.find_by_index(1)
    assert node.value == 20