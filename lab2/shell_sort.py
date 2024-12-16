# Функция сортировки методом Шелла
def shell_sort(arr, reverse=False):
    # Устанавливаем начальный интервал (gap)
    gap = len(arr) // 2

    # Основной цикл: продолжаем, пока gap не станет 0
    while gap > 0:
        # Проходим по массиву от gap до конца
        for value in range(gap, len(arr)):
            # Сохраняем текущий элемент и его индекс
            current_value = arr[value]
            pos = value

            # Если выбран reverse (по убыванию)
            if reverse:
                # Переставляем элементы, пока предыдущий меньше текущего
                while pos >= gap and arr[pos - gap] < current_value:
                    arr[pos] = arr[pos - gap]
                    pos -= gap
            else:
                # Иначе переставляем элементы, пока предыдущий больше текущего
                while pos >= gap and arr[pos - gap] > current_value:
                    arr[pos] = arr[pos - gap]
                    pos -= gap

            # Вставляем текущий элемент на его новое место
            arr[pos] = current_value

        # Уменьшаем gap для следующей итерации
        gap //= 2

    return arr