# Функция, реализующая сортировку пузырьком
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Интерфейс программы для взаимодействия с пользователем
def interface():
    print('Эта программа использует сортировку пузырьком (bubble sort)')
    print('Введите числа через пробел:')
    while True:
        try:
            arr = list(map(int, input().split()))
        except ValueError as e:
            print(f'Возникла ошибка: {e}. Повторите ввод.')
            continue
        if not arr:
            print('Ввод пустой. Введите снова:')
            continue
        else:
            print(f'Готово! Ваш отсортированный массив: {bubble_sort(arr)}')
            break

if __name__ == '__main__':
    interface()