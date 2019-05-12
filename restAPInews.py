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
    f'q={q}'
    f'country={country}&'
    f'pageSize={pageSize}&'
    f'page = {page}'
    f'apiKey={TOKEN}&'
    ) 

def reqwKeyW(mode, country, TOKEN, pageSize, page, q):
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
    f'country={country}&'
    f'pageSize={pageSize}&'
    f'page = {page}'
    f'apiKey={TOKEN}&'
    ) 

def reqw():
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
    f'country={country}&'
    f'pageSize={pageSize}&'
    f'page = {page}'
    f'apiKey={TOKEN}&'
    ) 

TOKEN = '34c8180e516a42159122bb8040ce0511'
if (debug):
    country = 'ru'
    language = 'ru'
    pageSize = '20'
    page = '1'
    q = 'Путин'
else :
    country = input()
    language = input()
    pageSize = input()  
    page = input()
    q = input()
mode = 'top-headlines'
# mode = 'everything'

response = reqwKeyW(mode, country, TOKEN, pageSize, page, q)

pprint.pprint(response.json())
