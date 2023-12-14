import numpy as np

def find_n_largest_and_smallest(matrix, n):
    # Разворачиваем матрицу в одномерный массив
    flattened_matrix = matrix.flatten()

    # Находим N наибольших и наименьших значений
    n_largest = np.partition(flattened_matrix, -n)[-n:]
    n_smallest = np.partition(flattened_matrix, n-1)[:n]

    return n_largest, n_smallest

# Пример использования
n_value = 5
matrix = generate_matrix(n_value)
n = 3  # Выбираем, например, 3 наибольших и наименьших значения

n_largest_values, n_smallest_values = find_n_largest_and_smallest(matrix, n)

print(f"{n} наибольших значений:", n_largest_values)
print(f"{n} наименьших значений:", n_smallest_values)
