def quick_sort(arr, l, r):
    if l >= r:
        return arr
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    quick_sort(arr, l, i)      # левая часть
    quick_sort(arr, i+2, r)    # правая часть
    return arr

# интерфейс программы для взаимодействия с пользователем
def interface():
    print('Эта программа использует быструю сортировку (quick sort)')
    while True:
        try:
            arr = list(map(int, input('Введите числа через пробел: ').split()))
            l = 0
            r = len(arr) - 1
        except ValueError as e:
            print(f'Возникла ошибка: {e}. Повторите ввод.')
            continue
        if not arr:
            print('Ввод пустой. Введите снова:')
            continue
        else:
            print(f'Готово! Ваш отсортированный массив: {quick_sort(arr, l, r)}')
            break

if __name__ == '__main__':
    interface()