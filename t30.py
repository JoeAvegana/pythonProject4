n = int(input('кол-во элементов '))
x = int(input('а[0]'))
d = int(input('шаг'))
print(*range(x, x + d * n, d))
