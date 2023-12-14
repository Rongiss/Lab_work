import numpy as np

N = 2
size = N * 5

# Создаем трехмерный массив
my_array = np.random.random((size, size, size))

# Находим индексы N*10 элемента
flat_index = N * 10
indices = np.unravel_index(flat_index, my_array.shape)

# Выводим результат
print("Индексы N*10 элемента:", indices)
