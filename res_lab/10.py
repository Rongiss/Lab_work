import numpy as np

# Задаем значение N
N = 2

# Создаем вектор со значениями от N*5 до N*10
vector = np.arange(N * 5, N * 10 + 1)

# Отсортировать вектор в обратном порядке
sorted_vector_reverse = np.sort(vector)[::-1]

# Вывод результатов
print("Исходный вектор:")
print(vector)

print("\nОтсортированный вектор в обратном порядке:")
print(sorted_vector_reverse)
