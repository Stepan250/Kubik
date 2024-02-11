list = 'РУНЕорутдышгНТРИРлыаооРОВЛАло'
list_2 = ''

for i in list:
    if not i.isupper():
        list_2 += i

print(f"символы нижнего регистра: {list_2}")



input_str = "ываПываываывркнекенивьбллрТпкенекн."

filtered_str = ''.join(filter(str.isalpha, input_str)).lower()

unique_letters = set(filtered_str)

target_letters = set(['п', 'р', 'и', 'в', 'е', 'т'])

#сделать задание со звездочкой