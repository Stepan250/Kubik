alphabet_upper = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 
                  'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 
                  'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 
                  'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

for letter_upper in alphabet_upper:
    letter_lower = letter_upper.lower()
    print(f"{letter_upper, letter_lower}, ||, {letter_upper, letter_lower} ||, {letter_upper, letter_lower}")