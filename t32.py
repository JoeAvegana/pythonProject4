import random
list = [random.randint(0, 100) for _ in range(10)]
print(list)
min = int(input('диапазон min '))
max = int(input('диапазон max '))
res = [index for index, value in enumerate(list) if min <= value <= max]
print(res)