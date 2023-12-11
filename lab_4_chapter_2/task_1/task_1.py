def b_above_zero(a, b, d):
    c = max(a, b, d) / a
    return c


def b_less_than_zero(a, b, d):
    c = max(a, b, d) / b
    return c


def b_equal_to_zero(a, d):
    c = (a + d) / min(a, d)
    return c


def main():
    a, b, d = (int(input()) for i in range(3))
    if b > 0:
        print(b_above_zero(a, b, d))
    elif b < 0:
        print(b_less_than_zero(a, b, d))
    else:
        print(b_equal_to_zero(a, d))


if __name__ == '__main__':
    main()
