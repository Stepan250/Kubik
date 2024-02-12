alphabet_upper = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 
                  'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 
                  'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 
                  'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


columns = 3
letters_per_column = len(alphabet_upper) // columns

for i in range(0, len(alphabet_upper), columns):
    row = alphabet_upper[i:i + columns]
    row_lower = [letter.lower() for letter in row]

    print("^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f"{row[0] + " " + row_lower[0]:^6} || {row[1] + " " + row_lower[1]:^6} || {row[2] + " " + row_lower[2]:^6}")

print("^^^^^^^^^^^^^^^^^^^^^^^^^")