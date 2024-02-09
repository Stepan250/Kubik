list = [10, 20, -30, 120, 36, 3, -6, 35]

list_2 = []

for i in list:
    if abs(i) > 20:
        list_2.append(i)

print(f"числа которые больше 20 по модулю: {list_2}")

list_1 = [10, 21, -30, 120, 36, 3, -60, 35, 70]
list_3 = []
for i in range(0, len(list_1) - 2, 2):
    number_1 = list_1[i]
    number_2 = list_1[i + 2]
    number_sum = number_1 + number_2

    if number_sum < list_1[i + 1]:
        list_3.append(list_1[i + 1])
print(f"среднии числа которое больше суммы соседних {list_3}")