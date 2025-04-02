import requests
from bs4 import BeautifulSoup

#Отправляет запрос в поисковую систему Bing и возвращает HTML страницу."""
def fetch_html(query, page):
    # Кодируем поисковый запрос для URL
    query = '+'.join(query.split())
    # Формируем URL для Bing поиска
    url = f'https://www.bing.com/search?q={query}&first={page * 10 + 1}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Отправляем запрос и проверяем статус
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Страница {page + 1} загружена успешно.")
        return response.text
    else:
        print(f"Ошибка при загрузке страницы {page + 1}: {response.status_code}")
        return None


def parse_results(html, page):
    #Парсит HTML и возвращает список результатов.
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    # Поиск всех элементов с результатами поиска
    for item in soup.find_all('li', class_='b_algo'):
        title = item.find('h2')
        link = item.find('a', href=True)

        if title and link:
            results.append({
                'page': page + 1,
                'url': link['href'],
                'title': title.get_text()
            })

    return results


def get_search_results(query, num_pages=2):
    #Получает ссылки и заголовки из результатов поиска Bing на 2 страницах.
    all_results = []

    for page in range(num_pages):
        html = fetch_html(query, page)
        if html:
            results = parse_results(html, page)
            all_results.extend(results)

    return all_results


def main():
    query = input("Введите поисковый запрос: ")
    results = get_search_results(query)

    # Проверка, есть ли результаты
    if not results:
        print("Нет результатов.")
    else:
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
