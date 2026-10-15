from avltree import AVLtree

def test_add_single():
    tree = AVLtree()
    tree.add(5)
    assert tree.to_list() == [5]

def test_add_keeps_order():
    tree = AVLtree()
    for x in [10, 5, 15, 3, 7]:
        tree.add(x)
    assert tree.to_list() == [3, 5, 7, 10, 15]

def test_add_rotation_ll():
    tree = AVLtree()
    for x in [30, 20, 10]:
        tree.add(x)
    assert tree.to_list() == [10, 20, 30]
    assert tree.root.value == 20

def test_add_rotation_rr():
    tree = AVLtree()
    for x in [10, 20, 30]:
        tree.add(x)
    assert tree.to_list() == [10, 20, 30]
    assert tree.root.value == 20

def test_add_rotation_lr():
    tree = AVLtree()
    for x in [30, 10, 20]:
        tree.add(x)
    assert tree.to_list() == [10, 20, 30]
    assert tree.root.value == 20

def test_add_rotation_rl():
    tree = AVLtree()
    for x in [10, 30, 20]:
        tree.add(x)
    assert tree.to_list() == [10, 20, 30]
    assert tree.root.value == 20

def test_search_found():
    tree = AVLtree()
    for x in [10, 5, 15]:
        tree.add(x)
    assert tree.search(10) is True
    assert tree.search(5) is True

def test_search_not_found():
    tree = AVLtree()
    for x in [10, 5, 15]:
        tree.add(x)
    assert tree.search(99) is False
    assert tree.search(7) is False


