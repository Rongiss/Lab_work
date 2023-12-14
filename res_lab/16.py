import numpy as np
from scipy.stats import mode

def generate_matrix(n):
    # Создаем матрицу N*5xN*5, заполняем случайными числами включая нули
    matrix = np.random.randint(0, 10, size=(n*5, n*5))
    return matrix

def find_most_and_least_common(matrix):
    # Разворачиваем матрицу в одномерный массив
    flattened_matrix = matrix.flatten()

    # Находим наиболее частое и наименее частое значение
    most_common = mode(flattened_matrix).mode[0]
    least_common = mode(flattened_matrix).mode[-1]

    return most_common, least_common

# Пример использования
n_value = 5
matrix = generate_matrix(n_value)
most_common_value, least_common_value = find_most_and_least_common(matrix)

print("Наиболее частое значение:", most_common_value)
print("Наименее частое значение:", least_common_value)
