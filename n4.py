#не знаю надо ли делать сохранение в отдельный файл. сейчас при новом запуске программы словарь снова пустой

print("Русско-английский словарь")

# Инициализация словаря
dictionary = {
    "кошка": "cat",
    "собака": "dog",
    "молоко": "milk",
    "яблоко": "apple"
}

while True:
    word = input("Введите интересующее русское слово (или 'выход' для завершения, 'словарь' для вывода всех слов): ").lower()
    if word == "выход":
        break
    if word == "словарь":
        for word, translation in sorted(dictionary.items()):
            print(f"{word} - {translation}")
    elif word in dictionary:
        print(f"Перевод слова '{word}' - {dictionary[word]}")
    else:
        print(f"Слово '{word}' отсутствует в словаре.")
        add_word = input("Хотите добавить его? (напишите да/нет): ").lower()
        if add_word == "да":
            translation = input(f"Введите перевод слова '{word}': ")
            dictionary[word] = translation
            print(f"Слово '{word}' добавлено в словарь.")
        else:
            print("Слово не добавлено.")
