# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]

import random
N = int(input())
lst = [random.randint(0, 5) for i in range(N)]
print(lst)
reester = []
for i in range(len(lst)):
    if lst[i] not in reester:
        reester.append(lst[i])
print(reester)
