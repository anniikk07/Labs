import numpy as np

class Array:
    def __init__(self, arr):
        self.arr = np.array(arr, dtype=np.int32)

    def add_to_tail(self, a):
        self.arr = np.append(self.arr, a)
        return self.arr

# реализую по шагам, чтобы лучше понять структуру
# намеренно не буду использовать встроенные фукнции
    def add_by_index(self, index, a):
        c = np.zeros(len(self.arr)+1, dtype=self.arr.dtype)
        c[:index] = self.arr[:index]
        c[index] = a
        c[index+1:] = self.arr[index:]
        self.arr = c
        return self.arr

    def remove_by_index(self, index):
        c = np.zeros(len(self.arr)-1, dtype=self.arr.dtype)
        c[:index] = self.arr[:index]
        c[index:] = self.arr[index+1:]
        self.arr = c
        return self.arr

    def find_by_index(self, index):
        ans = self.arr[index]
        return ans

    def find_by_value(self, a):
        for i in range(len(self.arr)):
            if self.arr[i] == a:
                return i
        return 'Ничего не найдено'

    def __eq__(self, other):
        return list(self.arr) == list(other)

# простой интерфейс для реализации этого кода пользователем

def create():
    print('Этот код будет демонстрировать работу с массивом')
    my_arr = []
    while my_arr == []:
        try:
            my_arr = Array(list(map(int, input('Заполните массив: ').split())))
            if my_arr.arr.size == 0:
                print('Ввод пуст. Попробуйте снова!')
                my_arr = []
        except ValueError as e:
            print(f'Возникла ошибка: {e}. Повторите ввод!')
        else:
            return my_arr
def interface(my_arr):
    print('\n_______________________________________________________________')
    print('1. Добавить число в конец          2. Добавить число по индексу')
    print('3. Удалить число по индексу        4. Найти число по индексу')
    print('5. Найти индекс по значению числа  6. Выйти из программы')
    choise = int(input('Выберите действие: '))

    if choise == 1:
        a = int(input('Введите добавляемое число: '))
        my_arr.add_to_tail(a)
        print('Полученный массив:', my_arr.arr)
    elif choise == 2:
        index = int(input('Введите индекс: '))
        a = int(input('Введите добавляемое число:'))
        my_arr.add_by_index(index, a)
        print('Полученный массив:', my_arr.arr)
    elif choise == 3:
        index = int(input('Введите индекс: '))
        my_arr.remove_by_index(index)
        print('Полученный массив:', my_arr.arr)
    elif choise == 4:
        index = int(input('Введите индекс: '))
        ans = my_arr.find_by_index(index)
        print('Найденное число:', ans)
    elif choise == 5:
        a = int(input('Введите искомое число:'))
        ans = my_arr.find_by_value(a)
        print('Индекс искомого числа:', ans)
    elif choise == 6:
        print('Выход из программы.')
        exit()
    else:
        print('Неверный пункт меню.')


if __name__ == '__main__':
    my_arr = create()
    while True:
        try:
            interface(my_arr)
        except Exception as e:
            print(f'Возникла ошибка: {e}! Повторите ввод.')