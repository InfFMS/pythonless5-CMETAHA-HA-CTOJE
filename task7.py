# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]

import random
N = int(input('N >> '))
lst = [random.randint(-100, 100) for i in range(N)]
print(lst)

lst_minus_and_zero = []
i = 0
while i <= len(lst)-1:
    if lst[i] <= 0:
        lst_minus_and_zero.append(lst[i])
        lst.pop(i)
    else:
        i += 1

print(lst + lst_minus_and_zero)
