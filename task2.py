# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5

import random
N = int(input())
lst = [random.randint(0, 5) for i in range(N)]
print(lst)

trig = 0
for i in range(len(lst)-1):
    if lst[i+1] == lst[i]:
        print(f'значение: {lst[i]} индексы: {i}, {i+1}')
        trig = 1

if trig == 0:
    print('Нет')
