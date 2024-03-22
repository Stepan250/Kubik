word = "апельсин"
prompts = ["оно съедобное", "это цитрус", "оно оранжевого цвета"]
max_attempts = 5
attempts = 0

print("Давай поиграем в угадайку!")
print("У тебя есть 5 попыток, чтобы угадать слово.")

while attempts < max_attempts:
    guess = input("Попробуй угадать кодовое слово: ").strip().lower()
    
    if guess == word:
        print(f"Поздравляю! Ты угадал кодовое слово: {word}!")
        break
    else:
        print("Неправильно.")
        if attempts < len(prompts):
            print(f"Подсказка: {prompts[attempts]}")
        else:
            print("У тебя закончились подсказки.")
        print("==================================")
        attempts += 1
else:
    print(f"К сожалению, ты исчерпал все попытки. Загаданное слово было: {word}.")

#сдать