
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def check_value(self, value):
        if type(value) is not int:
            raise ValueError('Это не целое число!')

    def check_index(self, index):
        self.check_value(index)
        if 0 > index or index >= self.size:
            raise IndexError(f'Индекс вне диапазона! ')

    def add_to_head(self, value):
        self.check_value(value)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_by_index(self, value, index):
        self.check_value(value)
        if index == 0:
            self.add_to_head(value)
            return
        self.check_index(index)
        if index == self.size:
            self.add_to_tail(value)
            return
        new_node = Node(value)
        n = self.head
        for i in range(index):
            n = n.next
        new_node.prev = n.prev
        new_node.next = n
        n.prev = new_node
        new_node.prev.next = new_node
        self.size += 1

    def add_to_tail(self, value):
        self.check_value(value)
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def remove_from_head(self):
        if self.head is None:
            print ('Список пуст!')
            return
        if self.head == self.tail:
            print('В списке был только один элемент!')
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def remove_by_index(self, index):
        if self.head is None:
            print ('Список пуст!')
            return
        if self.head == self.tail:
            self.check_index(index)
            print('В списке был только один элемент!')
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.check_index(index)
            if index == 0:
                self.remove_from_head()
            elif index == self.size-1:
                self.remove_from_tail()
            else:
                n = self.head
                for i in range(index):
                    n = n.next
                n.prev.next = n.next
                n.next.prev = n.prev
                n.prev = None
                n.next = None
                self.size -= 1




    def remove_from_tail(self):
        if self.tail is None:
            print('Список пуст!')
            return
        if self.head == self.tail:
            print('В списке был только один элемент!')
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def find_by_value(self, value):
        self.check_value(value)
        n = self.head
        for i in range(self.size):
            if n.value == value:
                return i
            n = n.next
        return None

    def find_by_index(self, index):
        self.check_index(index)
        n = self.head
        for i in range(index):
            n = n.next
        return n

    def __str__(self):
        if self.head is None:
            return "[]"
        n = self.head
        nodes = []
        while n is not None:
            nodes.append(str(n.value))
            n = n.next
        return ' <-> '.join(nodes)

def create():
    print('Этот код будет демонстрировать работу со связным списком')
    your_list = List()
    while True:
        try:
            raw = input('Заполните список: ').strip()
            if raw:
                for val in map(int, raw.split()):
                    your_list.add_to_tail(val)
            return your_list
        except ValueError as e:
            print(f'Возникла ошибка: {e} Повторите ввод!')


def interface(your_list):
    print('\n_______________________________________________________________')
    print('1. Добавить число в начало       2. Добавить число по индексу')
    print('3. Добавить число в конец        4. Удалить число из начала')
    print('5. Удалить число по индексу      6. Удалить число из конца')
    print('7. Найти число по индексу        8. Найти индекс по числу')
    print('0. Выйти из программы')
    choise = int(input('Выберите действие: '))

    if choise == 1:
        a = int(input('Введите добавляемое число: '))
        your_list.add_to_head(a)
        print('Полученный список:', your_list)
    elif choise == 2:
        index = int(input('Введите индекс: '))
        a = int(input('Введите добавляемое число: '))
        your_list.add_by_index(a, index)
        print('Полученный список:', your_list)
    elif choise == 3:
        a = int(input('Введите добавляемое число: '))
        your_list.add_to_tail(a)
        print('Полученный список:', your_list)
    elif choise == 4:
        your_list.remove_from_head()
        print('Полученный список:', your_list)
    elif choise == 5:
        index = int(input('Введите индекс: '))
        your_list.remove_by_index(index)
        print('Полученный список:', your_list)
    elif choise == 6:
        your_list.remove_from_tail()
        print('Полученный список:', your_list)
    elif choise == 7:
        index = int(input('Введите индекс: '))
        ans = your_list.find_by_index(index)
        print('Найденное число:', ans.data)
    elif choise == 8:
        a = int(input('Введите искомое число: '))
        n = your_list.head
        idx = -1
        current_idx = 0
        while n is not None:
            if n.data == a:
                idx = current_idx
                break
            n = n.next
            current_idx += 1
        if idx == -1:
            print('Такого числа в списке нет.')
        else:
            print('Индекс искомого числа:', idx)
    elif choise == 0:
        print('Выход из программы.')
        exit()
    else:
        print('Неверный пункт меню.')


if __name__ == '__main__':
    list = create()
    while True:
        try:
            interface(list)
        except (TypeError, ValueError, IndexError) as e:
            print('Возникла ошибка:', e)