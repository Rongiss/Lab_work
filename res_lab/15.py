import numpy as np

def diagonal_elements(matrix1, matrix2):
    # Проверка, что число столбцов первой матрицы равно числу строк второй матрицы
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Невозможно умножить матрицы: неправильные размерности")

    # Умножение матриц
    result_matrix = np.dot(matrix1, matrix2)

    # Получение элементов главной диагонали
    diag_elements = [result_matrix[i, i] for i in range(min(len(result_matrix), len(result_matrix[0])))]

    return diag_elements

# Пример использования
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

result = diagonal_elements(matrix_a, matrix_b)
print("Диагональные элементы произведения матриц:", result)
