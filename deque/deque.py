import numpy as np


class Deque:

    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Размер должен быть положительным")
        self.size = size
        self.data = np.zeros(size, dtype=np.int32)
        self.head = 0
        self.tail = 0
        self.count = 0

    def FillTheDeque(self, numbers: list[int]) -> None:
        n = min(len(numbers), self.size)
        self.data[:n] = numbers[:n]
        self.head = 0
        self.tail = n % self.size
        self.count = n

    def AddToHead(self, x: int) -> None:
        if self.count == self.size:
            raise OverflowError("Дек заполнен")
        self.head = (self.head - 1) % self.size
        self.data[self.head] = x
        self.count += 1

    def AddToTail(self, x: int) -> None:
        if self.count == self.size:
            raise OverflowError("Дек заполнен")
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def DeleteFromHead(self) -> int:
        if self.count == 0:
            raise IndexError("Дек пуст")
        x = self.data[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return int(x)

    def DeleteFromTail(self) -> int:
        if self.count == 0:
            raise IndexError("Дек пуст")
        self.tail = (self.tail - 1) % self.size
        x = self.data[self.tail]
        self.count -= 1
        return int(x)

    def GetByIndex(self, index: int) -> int:
        if index < 0 or index >= self.count:
            raise IndexError("Индекс вне диапазона")
        real_index = (self.head + index) % self.size
        return int(self.data[real_index])

    def Show(self) -> list[int]:
        return [int(self.data[(self.head + i) % self.size]) for i in range(self.count)]


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Нужно ввести целое число! Попробуйте снова.")


def read_deque() -> Deque:
    size = read_int("Размер дека: ")
    d = Deque(size)

    print("Введите числа через пробел:")
    while True:
        try:
            numbers = list(map(int, input().split()))
            d.FillTheDeque(numbers)
            return d
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")

def print_deque(d: Deque) -> None:
    items = d.Show()
    if not items:
        print("Дек пуст")
    else:
        print("Дек: [" + ", ".join(map(str, items)) + "]")

def interface(d: Deque) -> bool:
    menu = (
        "\n1. Добавить в начало    2. Добавить в конец\n"
        "3. Удалить сначала      4. Удалить с конца\n"
        "5. Найти по индексу     6. Показать дек\n"
        "0. Выход"
    )
    print(menu)
    choise = input("Выбор: ").strip()

    try:
        if choise == "0":
            print("Выход.")
            return False

        elif choise == "1":
            x = read_int("Число: ")
            d.AddToHead(x)
            print(f"Добавлено {x} в начало")

        elif choise == "2":
            x = read_int("Число: ")
            d.AddToTail(x)
            print(f"Добавлено {x} в конец")

        elif choise == "3":
            x = d.DeleteFromHead()
            print(f"Удалён {x} из начала")

        elif choise == "4":
            x = d.DeleteFromTail()
            print(f"Удалён {x} из конца")

        elif choise == "5":
            idx = read_int("Индекс: ")
            value = d.GetByIndex(idx)
            print(f"Элемент [{idx}] = {value}")

        elif choise == "6":
            print_deque(d)

        else:
            print("Неверная команда!")

    except (OverflowError, IndexError) as e:
        print(f"Ошибка: {e}")

    return True


def main():
    d = read_deque()

    while True:
        if not interface(d):
            break


if __name__ == "__main__":
    main()