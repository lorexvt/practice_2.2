"""
Разработайте утилиту, которая выполняет HTTP-запросы GET к данным
адресам:
1) https://github.com/
2) https://www.binance.com/en
3) https://tomtit.tomsk.ru/
4) https://jsonplaceholder.typicode.com/
5) https://moodle.tomtit-tomsk.ru/
и определяет их статус по кодам ответа сервера (200, 404, 500 и другие).
Формат вывода программы:
URL – доступность(доступен/не доступен/вход запрещен/не найден) –
код ответа.
"""

import requests


sites = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

print("Результаты проверки сайтов:")
print("=" * 50)

for site in sites:
    try:
        response = requests.get(site, timeout=5)
        code = response.status_code

        if code == 200:
            status = "Доступен"
        elif code == 403:
            status = "Вход запрещен"
        elif code == 404:
            status = "Не найден"
        else:
            status = f"Код {code}"

    except:
        status = "Не доступен"
        code = "Ошибка"

    print(f"{site} – {status} – {code}")

print("=" * 50)