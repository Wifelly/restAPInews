import requests
import pprint


def req(county='ru', pageSize='20', page='1', TOKEN=None):
    return requests.get(
                        f'https://newsapi.org/v2/top-headlines?'
                        f'country={country}&'
                        f'pageSize={pageSize}&'
                        f'page={page}&'
                        f'apiKey={TOKEN}'
    )


def reqCat(category, country='ru', pageSize=20, page=1, TOKEN=None):
    return requests.get(
                        f'https://newsapi.org/v2/top-headlines?'
                        f'country={country}&'
                        f'category={category}&'
                        f'pageSize={pageSize}&'
                        f'page={page}&'
                        f'apiKey={TOKEN}'
    )


def reqKeyW(q, country='ru', pageSize=20, page=1, TOKEN=None):
    return requests.get(
                        f'https://newsapi.org/v2/top-headlines?'
                        f'q={q}&'
                        f'country={country}&'
                        f'pageSize={pageSize}&'
                        f'page={page}&'
                        f'apiKey={TOKEN}'
    )

TOKEN = '34c8180e516a42159122bb8040ce0511'
debug = True

if (debug):
    country = 'ru'
    language = 'ru'
    pageSize = '20'
    page = '1'
    q = 'Путин'
    category = 'general'
else:
    country = input()
    language = input()
    pageSize = input()
    page = input()
    q = input()
    category = input()

cont = True
while(cont):
    print('enter mode:\n'
        '1 - request\n'
        '2 - request category\n'
        '3 - request key wrd\n'
        )
    mode = input()
    if mode == '1':
        response = req(country, pageSize, page, TOKEN)
    elif mode == '2':
        response = reqCat(category, country, pageSize, page, TOKEN)
    elif mode == '3':
        response = reqKeyW(q, country, pageSize, page, TOKEN)
    pprint.pprint(response.json())
    print('cont?\n y/n')
    temp_cont = input()
    if temp_cont == 'n':
        cont = False
