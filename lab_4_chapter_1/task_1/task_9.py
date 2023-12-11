# 9. Ввести с клавиатуры строку символов. Программа должна определить длину
# введенной строки L, и, если длина L кратна 5, то подсчитывается количество скобок всех
# видов.

def main() -> None:

    string: str = input('Input - ')
    sym_c = '(){}[]'

    if len(string) % 5 == 0:
        for i in sym_c:
            print(f'Количесво {i} - {string.count(i)}')
    else:
        print('Строка не кратна 5!')


if __name__ == '__main__':
    main()
