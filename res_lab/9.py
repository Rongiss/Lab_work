import numpy as np

# Задаем размерность
N = 3

# Создаем две матрицы размерности N*5xN*3 и заполняем случайными числами
matrix1 = np.random.random((N * 5, N * 3))
matrix2 = np.random.random((N * 5, N * 3))

# Перемножение матриц с использованием np.dot
result_dot = np.dot(matrix1, matrix2.T)  # .T - транспонирование второй матрицы

# Перемножение матриц с использованием @ оператора (доступно в Python 3.5 и выше)
result_at = matrix1 @ matrix2.T

# Перемножение матриц с использованием np.matmul
result_matmul = np.matmul(matrix1, matrix2.T)

# Вывод результатов
print("Перемножение с использованием np.dot:")
print(result_dot)

print("\nПеремножение с использованием @ оператора:")
print(result_at)

print("\nПеремножение с использованием np.matmul:")
print(result_matmul)
