# Функция, реализующая сортировку пузырьком
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Интерфейс программы для взаимодействия с пользователем
print('Эта программа использует сортировку пузырьком (bubble sort)')
print('Введите числа через пробел:')
try:
    arr = list(map(int, input().split()))
    print(f'Готово! Ваш отсортированный массив: {bubble_sort(arr)}')
except Exception as e:
    print(f'Возникла ошибка: {e}. Повторите ввод.')