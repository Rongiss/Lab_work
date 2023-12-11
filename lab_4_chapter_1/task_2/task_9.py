a = [i ** 2 + 1 if i % 2 != 0 else i * 2 - 1 for i in range(10)]
d = [i * 2.5 if i < 2.5 else i / 2.5 for i in range(10)]
print(d)
