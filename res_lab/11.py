import numpy as np

def generate_arrays(size):
    array1 = np.random.randint(0, 10, size)
    array2 = np.random.randint(0, 10, size)
    return array1, array2

def edit_array(array):
    print("Текущий массив:", array)
    index = int(input("Введите индекс элемента для изменения (от 0 до {}): ".format(len(array)-1)))
    value = int(input("Введите новое значение: "))
    array[index] = value
    print("Массив после изменения:", array)

def check_arrays_equal(array1, array2):
    return np.array_equal(array1, array2)

# Задаем размер массивов
size = 5

# Генерируем два массива
arr1, arr2 = generate_arrays(size)

# Печать сгенерированных массивов
print("Первый массив:", arr1)
print("Второй массив:", arr2)

# Вручную изменяем элементы массивов
edit_array(arr1)
edit_array(arr2)

# Проверяем, одинаковы ли массивы
if check_arrays_equal(arr1, arr2):
    print("Массивы идентичны.")
else:
    print("Массивы различны.")
