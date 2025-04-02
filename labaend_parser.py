import requests
from bs4 import BeautifulSoup
from datetime import datetime


def parse_reestr_nostroy():
    url = 'https://torgi223.ru/reestr-zakupok/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    for row in soup.find_all('tr', class_='data-row'):
        name = row.find('td', class_='name').get_text(strip=True)
        description = row.find('td', class_='description').get_text(strip=True)
        categories = [cat.get_text(strip=True) for cat in row.find_all('td', class_='category')]
        date = row.find('td', class_='date').get_text(strip=True)
        amount = row.find('td', class_='amount').get_text(strip=True)

        data.append({
            'name': name,
            'description': description,
            'categories': categories,
            'date': datetime.strptime(date, '%d.%m.%Y'),
            'amount': float(amount.replace(',', '.'))
        })

    return data
