word = "апельсин"
prompt = ["оно съедобное", "это цитрус", "оно оранжевого цвета", ""]
max_promts = 0
for j in prompt:
    secret_word = input("Угадай кодовое слово: ")
    if secret_word == word:
        print(f"Ты угадал кодовое слово: {word}!")
    else:
        if max_promts <= 4:
            print("Нет такого слова")
            print(f"подсказка: {j}")
            print("==================================")
            max_promts += 1
