from random import randint


def fin_max_el_var_1(l: list) -> int:
    """
    Функция поиска максимального значения элемента массива вариант 1
    :param l: list
    :return: int
    """
    el = l[0]
    for i in l:
        if i >= el:
            el = i
    return el


def fin_max_el_var_2(l: list) -> int:
    """
    Функция поиска максимального значения элемента массива вариант 2
    :param l: list
    :return: int
    """
    return max(l)


def main():
    """
    Главная функция нахлждения суммы элементов массива,
    расположенных до последнего положительного элемента.
    :return:
    """
    lis = [randint(0, 1000) for i in range(10)]
    print(lis)
    print(fin_max_el_var_2(lis))


def sum_al_var_1():
    """
    Главная функция нахлждения суммы элементов массива,
    расположенных до последнего положительного элемента. Вариант 1
    :return: None
    """
    li = [-5, -6, 5, -8, 5, -6, -1]
    inde = ''
    for i in li[::-1]:
        if i > 0:
            inde = -(li.index(i) + 1)
            break
    print(sum(li[:inde]))


def sum_al_var_2():
    """
    Главная функция нахлждения суммы элементов массива,
    расположенных до последнего положительного элемента. Вариант 2
    :return: None
    """
    li = [-5, -6, 5, -8, 5, -6, -1]
    inde = ''
    total = 0

    for i in li[::-1]:
        if i > 0:
            inde = -(li.index(i) + 1)
            break

    for i in li[:inde]:
        total += i
    print(total)


def zip_matrix():
    """
    Сжать массив, удалив из него все элементы, модуль которых находится в интервале [а, b].
    Освободившиеся в конце массива элементы заполнить нулями.
    :return: none
    """

    lis = [randint(0, 1000) for i in range(10)]

    a = 100
    b = 400
    total = 0
    for i in lis:
        if a <= i <= b:
            total += 1
            lis.remove(i)

    for i in range(total):
        lis.append(0)

    print(lis)


if __name__ == '__main__':
    zip_matrix()
