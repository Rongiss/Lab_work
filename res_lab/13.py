import numpy as np


def find_nearest(array, value):
    """
    Находит ближайшее число к заданному значению в массиве.

    Параметры:
    - array: numpy array, входной массив чисел.
    - value: число, для которого ищем ближайшее значение.

    Возвращает:
    - nearest_value: ближайшее значение к заданному.
    """
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    nearest_value = array[idx]
    return nearest_value


# Пример использования
if __name__ == "__main__":
    # Создаем случайный массив
    random_array = np.random.randint(0, 100, 10)

    # Задаем значение, для которого будем искать ближайшее
    target_value = 42

    # Ищем ближайшее значение
    nearest = find_nearest(random_array, target_value)

    print(f"Исходный массив: {random_array}")
    print(f"Ближайшее значение к {target_value}: {nearest}")
