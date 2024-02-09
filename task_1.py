list = [2981, 213, 32, 29, -32, -19, 3, 20]
list_2 = []

for i in list:
    if abs(i) > 20:
        list_2.append(i)
print(list_2)