from datetime import datetime
import textwrap

title = input("Введите заголовок новости: ")
news = input("Введите основной текст новости: ")

current_date = datetime.now().strftime("%d.%m.%Y") #текущая дата
word_count = len(news.split())+len(title.split())+1 #плюс 1 делаем, чтобы считалась дата за кол-во слов. в условии задачи 37 слов.
page_width = 80 #ширина страницы
wrapped_news = textwrap.fill(news, width=page_width) # Перенос текста по ширине
centered_lines = [line.center(page_width) for line in wrapped_news.split('\n')] #центруем текст, список строк
centered_news = "\n".join(centered_lines) # Соединяем центрированные строки обратно в многострочный текст

# Форматированный вывод
print(f"{current_date:>{page_width}}")  # Дата в правом углу
print(f"{'«' + title.upper() + '»':^{page_width}}\n")  # Заголовок по центру
print(centered_news)
print("-" * page_width)
print(f"Количество слов в тексте: {word_count}")

#пополнение
#Большая панда в зоопарке Японии принесла потомство. При этом у нее вместо одного родилось сразу два детеныша. Близнецы появились на свет в парке "Вакаяма". С разницей в 3 часа. Каждый весит приблизительно по 180 граммов.
