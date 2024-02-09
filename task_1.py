list = [21, 213, 32, 29, -32, -19, 3, 20, 170, 283, 321, 1, 451, 3123, 3213, 312, 4843, 4823, 20, 21]

list_2 = []

for i in list:
    if abs(i) > 20:
        list_2.append(i)

print(f"числа которые больше 20 по модулю: {list_2}")

list_3 = []
for i in range(0, len(list) - 2, 2):
    number_1 = list[i]
    number_2 = list[i + 2]
    number_sum = number_1 + number_2

    if number_sum < list[i + 1]:
        list_3.append(list[i + 1])
print(f"среднии числа которое больше суммы соседних {list_3}")