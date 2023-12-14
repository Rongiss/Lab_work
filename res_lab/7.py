import numpy as np

N = 5  # Замените 5 на любое число, которое вы хотите использовать

# Создаем случайный вектор размера N*15
random_vector = np.random.random(N * 15)

# Находим среднее значение элементов вектора
average_value = np.mean(random_vector)

# Выводим результат
print("Случайный вектор:", random_vector)
print("Среднее значение элементов:", average_value)
