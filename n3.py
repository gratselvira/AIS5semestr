import random

list = [random.randint(-50, 50) for _ in range(20)]
print("Список:", list)
new_list = [list[i] for i in range(0, len(list), 2) if list[i] < 0]
print("Отрицательные числа на нечётных местах:", new_list)

