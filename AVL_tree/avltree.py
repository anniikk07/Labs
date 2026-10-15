class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLtree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def get_bf(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, node):
        new_node = node.right
        l_kid = new_node.left
        new_node.left = node
        node.right = l_kid
        self.update_height(node)
        self.update_height(new_node)
        return new_node

    def right_rotate(self, node):
        new_node = node.left
        r_kid = new_node.right
        new_node.right = node
        node.left = r_kid
        self.update_height(node)
        self.update_height(new_node)
        return new_node

    def left_right_rotate(self, node):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def right_left_rotate(self, node):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def rotate(self, node):
        self.update_height(node)
        bf = self.get_bf(node)
        if bf > 1:
            if self.get_bf(node.left) >= 0:
                return self.right_rotate(node)
            return self.left_right_rotate(node)
        if bf < -1:
            if self.get_bf(node.right) <= 0:
                return self.left_rotate(node)
            return self.right_left_rotate(node)
        return node

    def check_value(self, a):
        if not isinstance(a, int) or isinstance(a, bool):
            raise TypeError(f'Число не целое!')

    def add(self, value):
        self.check_value(value)
        self.root = self._add(self.root, value)

    def _add(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._add(node.left, value)
        elif value > node.value:
            node.right = self._add(node.right, value)
        else:
            raise ValueError(f'Значение {value} уже есть в дереве')
        return self.rotate(node)

    def search(self, value):
        self.check_value(value)
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def to_list(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)

    def __str__(self):
        return str(self.to_list())
