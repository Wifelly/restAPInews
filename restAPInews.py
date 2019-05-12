# Реализовать набор функций для работы с API:
# - Получить последние публикации по списку категорий.
# - Получить последние публикации по списку ключевых слов.
# - Поиск публикаций по запросу.

# Функции должны предоставлять возможность пагинации (указания размера и номера страницы) и выбора страны/языка.

# Решение должно быть оформлено в виде репозитория на GitHub,
# в ответе нужно прикрепить ссылку на репозиторий.

debug = True

import requests, pprint

def reqwCat(mode, country, TOKEN, pageSize, page):
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
    f'country={country}&'
    f'apiKey={TOKEN}&'
    f'pageSize={pageSize}&'
    f'page = {page}'
    ) 

def reqwKeyW():
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
    f'country={country}&'
    f'apiKey={TOKEN}&'
    f'pageSize={pageSize}&'
    f'page = {page}'
    ) 

def reqw():
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
    f'country={country}&'
    f'apiKey={TOKEN}&'
    f'pageSize={pageSize}&'
    f'page = {page}'
    ) 

TOKEN = '34c8180e516a42159122bb8040ce0511'
if (debug):
    country = 'ru'
    language = 'ru'
    pageSize = '20'
    page = '1'
else :
    country = input()
    language = input()
    pageSize = input()  
    page = input()
mode = 'top-headlines'
# mode = 'everything'
# request = (
#     f'https://newsapi.org/v2/{mode}?'
#     f'country={country}&'
#     f'apiKey={TOKEN}&'
#     f'pageSize={pageSize}'
# )

response = reqwCat(mode, country, TOKEN, pageSize, page)

pprint.pprint(response.json())
