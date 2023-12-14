import numpy as np

N = 5  # Замените 5 на любое число, которое вы хотите использовать

# Создаем матрицу размера N*5 x N*5, заполненную случайными числами (включая нули)
my_matrix = np.random.rand(N * 5, N * 5)

for i in range(len(my_matrix)):
    for j in range(i):
        if my_matrix[i][j] != 0:
            print(i, j)
