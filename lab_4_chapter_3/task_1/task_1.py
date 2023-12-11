import numpy as np

# Размерность матрицы
N = 5

# Создаем две матрицы размерности N*5 и N*3
matrix1 = np.random.rand(N*5, N*3)
matrix2 = np.random.rand(N*3, N*5)

# Перемножение матриц с использованием NumPy
result_np = np.dot(matrix1, matrix2)

# Перемножение матриц вручную
result_manual = np.zeros((N*5, N*5))

for i in range(N*5):
    for j in range(N*5):
        result_manual[i, j] = sum(matrix1[i, k] * matrix2[k, j] for k in range(N*3))

# Вывод результата
print("Матрица 1:")
print(matrix1)
print("\nМатрица 2:")
print(matrix2)
print("\nРезультат перемножения с использованием NumPy:")
print(result_np)
print("\nРезультат перемножения вручную:")
print(result_manual)
