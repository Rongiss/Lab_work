import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


# Задаем параметры распределения
mu, sigma = 0, 0.1  # Среднее и стандартное отклонение

# Генерируем массив с распределением Гаусса
gaussian_array = np.random.normal(mu, sigma, 1000)

# Визуализируем распределение
plt.hist(gaussian_array, bins=50, density=True, alpha=0.6, color='g')
plt.title('Гистограмма распределения Гаусса')
plt.show()
