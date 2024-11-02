# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.

lst = list(map(int, input().split()))
prev_max = 0
count = 0
for i in range(len(lst)):
    if lst[i] > prev_max:
        prev_max = lst[i]
        count = 1
    elif lst[i] == prev_max:
        count += 1
print(count)