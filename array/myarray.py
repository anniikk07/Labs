import numpy as np

class Array:

    def __init__(self, arr):
        if len(arr) == 0:
            raise ValueError('Ввод пуст!')
        self.size = len(arr)
        self.capacity = max(self.size*2, 1)
        self.my_arr = np.zeros(self.capacity, dtype=np.int32)
        for i in range(self.size):
            self.check_value(arr[i])
            self.my_arr[i] = arr[i]

    def check_value(self, a):
        if not isinstance(a, (int, np.integer)) or isinstance(a, bool):
            raise TypeError(f'Число не целое! Полученный ввод: {a}')

    def check_index(self, index):
        self.check_value(index)
        if 0 > index or index >= self.size:
            raise IndexError(f'Индекс вне диапазона: [0, {self.size-1}]')

    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = np.zeros(self.capacity, dtype=np.int32)
        for i in range(self.size):
            new_arr[i] = self.my_arr[i]
        self.my_arr = new_arr

    def add_to_head(self, a):
        self.check_value(a)
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, 0, -1):
            self.my_arr[i] = self.my_arr[i - 1]
        self.my_arr[0] = a
        self.size += 1

    def add_by_index(self, index, a):
        self.check_value(a)
        self.check_index(index)
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.my_arr[i] = self.my_arr[i-1]
        self.my_arr[index] = a
        self.size += 1

    def add_to_tail(self, a):
        self.check_value(a)
        if self.size == self.capacity:  # место закончилось
            self.resize()
        self.my_arr[self.size] = a
        self.size += 1

    def remove_from_head(self):
        if self.size == 0:
            raise IndexError('Массив пуст, удалять нечего')
        for i in range(0, self.size-1):
            self.my_arr[i] = self.my_arr[i+1]
        self.size -= 1

    def remove_by_index(self, index):
        if self.size == 0:
            raise IndexError('Массив пуст, удалять нечего')
        self.check_index(index)
        for i in range(index, self.size-1):
            self.my_arr[i] = self.my_arr[i+1]
        self.size -= 1

    def remove_from_tail(self):
        if self.size == 0:
            raise IndexError('Массив пуст, удалять нечего')
        self.my_arr[self.size-1] = 0
        self.size -= 1

    def find_by_index(self, index):
        self.check_index(index)
        ans = self.my_arr[index]
        return ans

    def find_by_value(self, a):
        self.check_value(a)
        for i in range(self.size):
            if self.my_arr[i] == a:
                return i
        return None

    def __eq__(self, other):
        return list(self.my_arr[:self.size]) == list(other)

# простой интерфейс для реализации этого кода пользователем

def create():
    print('Этот код будет демонстрировать работу с массивом')
    your_arr = []
    while True:
        try:
            your_arr = Array(list(map(int, input('Заполните массив: ').split())))
        except ValueError as e:
            print(f'Возникла ошибка: {e} Повторите ввод!')
        else:
            return your_arr
def interface(your_arr):
    print('\n_______________________________________________________________')
    print('1. Добавить число в начало       2. Добавить число по индексу')
    print('3. Добавить число в конец        4. Удалить число из начала')
    print('5. Удалить число по индексу      6. Удалить число из конца')
    print('7. Найти число по индексу        8. Найти индекс по числу')
    print('0. Выйти из программы')
    choise = int(input('Выберите действие: '))

    if choise == 1:
        a = int(input('Введите добавляемое число: '))
        your_arr.add_to_head(a)
        print('Полученный массив:', your_arr.my_arr[:your_arr.size])
    elif choise == 2:
        index = int(input('Введите индекс: '))
        a = int(input('Введите добавляемое число:'))
        your_arr.add_by_index(index, a)
        print('Полученный массив:', your_arr.my_arr[:your_arr.size])
    elif choise == 3:
        a = int(input('Введите добавляемое число: '))
        your_arr.add_to_tail(a)
        print('Полученный массив:', your_arr.my_arr[:your_arr.size])
    elif choise == 4:
        your_arr.remove_from_head()
        print('Полученный массив:', your_arr.my_arr[:your_arr.size])
    elif choise == 5:
        index = int(input('Введите индекс: '))
        your_arr.remove_by_index(index)
        print('Полученный массив:', your_arr.my_arr[:your_arr.size])
    elif choise == 6:
        your_arr.remove_from_tail()
        print('Полученный массив:', your_arr.my_arr[:your_arr.size])
    elif choise == 7:
        index = int(input('Введите индекс: '))
        ans = your_arr.find_by_index(index)
        print('Найденное число:', ans)
    elif choise == 8:
        a = int(input('Введите искомое число:'))
        ans = your_arr.find_by_value(a)
        if ans is None:
            print('Такого числа в массиве нет.')
        else:
            print('Индекс искомого числа:', ans)
    elif choise == 0:
        print('Выход из программы.')
        exit()
    else:
        print('Неверный пункт меню.')


if __name__ == '__main__':
    arr = create()
    while True:
        try:
            interface(arr)
        except (TypeError, ValueError, IndexError) as e:
            print('Возникла ошибка:', e)