list = 'РУНЕорутдышгНТРИРлыаооРОВЛАло'
list_2 = ''

for i in list:
    if not i.isupper():
        list_2 += i

print(f"Символы нижнего регистра: {list_2}")




input_str = "ываПываываывркнекенивьбллрТпкенекн."
target_letters = ["П", "п", "Р", "р", "И", "и", "В", "в", "Е", "е", "Т", "т"]

letters = set()
list_letters = []
for j in target_letters:
    if j.lower() not in letters and j in input_str:
        letters.add(j.lower())
        list_letters.append(j)
print(f"Из этого набора символов получилось слово: {list_letters}")