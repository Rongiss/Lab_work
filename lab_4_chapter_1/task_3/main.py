import pprint, random


def generate_matrix():
    """
    Функция генерирует матрицу 6х6 запполненую рандомными целочисленными значениями
    :return: list
    """
    zero_matrix = [[0 for i in range(6)] for i in range(6)]
    for i in range(len(zero_matrix)):
        for j in range(len(zero_matrix[i])):
            zero_matrix[i][j] = random.randint(0, 9)
    return zero_matrix


def generete_matrix_d():

    a, b, c = (generate_matrix() for i in range(3))
    print("a")
    pprint.pprint(a)
    print("b")
    pprint.pprint(b)
    print("c")
    pprint.pprint(c)

    d = [[0 for i in range(6)] for i in range(6)]
    for i in range(len(d)):
        for j in range(len(d[i])):
            d[i][j] = max(a[i][j], b[i][j] + c[i][j])
    print("res")
    return d


pprint.pprint(generete_matrix_d())
