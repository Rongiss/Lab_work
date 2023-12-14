import numpy as np

def process_matrix(matrix):
    # Размеры исходной матрицы
    num_rows, num_columns = matrix.shape

    # Создаем матрицу для хранения результатов
    result_matrix = np.zeros((num_rows + 1, num_columns + 1), dtype=int)

    # Заполняем результаты
    for i in range(num_rows):
        for j in range(num_columns):
            result_matrix[i, j] = matrix[i, j]
            if matrix[i, j] == 0:
                result_matrix[i, num_columns] += 1
                result_matrix[num_rows, j] += 1

    return result_matrix

# Пример использования
N = 3
# Создаем пример матрицы
A = np.array([[1, 0, 2, 0],
              [0, 3, 0, 4],
              [5, 0, 6, 0]])

result_matrix = process_matrix(A)

# Выводим результат
print("Исходная матрица:")
print(A)
print("\nРезультат:")
print(result_matrix)
