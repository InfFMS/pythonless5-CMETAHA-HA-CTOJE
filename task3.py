# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3

import random
N = int(input('N >> '))
lst = [random.randint(0, 10) for i in range(N)]
# print(lst)
reester = []
for i in range(len(lst)):
    if lst.count(lst[i]) >= 2 and lst[i] not in reester:
        count = []
        reester.append(lst[i])
        for j in range(i, len(lst)):
            if lst[j] == lst[i]: count.append(str(j))
        print(f'значение: {lst[i]} индексы: {', '.join(count)}')
