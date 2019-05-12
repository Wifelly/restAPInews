debug = True

import requests, pprint

def req(county = 'ru', pageSize = '20', page = '1', TOKEN = None):
    return requests.get(
    f'https://newsapi.org/v2/top-headlines?'
    f'country={country}&'
    f'pageSize={pageSize}&'
    f'page = {page}&'
    f'apiKey = {TOKEN}'
    ) 

def reqCat(category, country = 'ru', pageSize = 20, page = 1, TOKEN = None):
    return requests.get(
    f'https://newsapi.org/v2/top-headlines?'
    f'country={country}&'
    f'category={category}&'
    f'pageSize={pageSize}&'
    f'page = {page}&'
    f'apiKey = {TOKEN}'
    ) 

def reqKeyW(q, country = 'ru', pageSize = 20, page = 1, TOKEN = None):
    return requests.get(
    f'https://newsapi.org/v2/top-headlines?'
    f'q={q}&'
    f'country={country}&'
    f'pageSize={pageSize}&'
    f'page = {page}&'
    f'apiKey = {TOKEN}'
    ) 

TOKEN = '34c8180e516a42159122bb8040ce0511'
if (debug):
    country = 'ru'
    language = 'ru'
    pageSize = '20'
    page = '1'
    q = 'Путин'
    category = 'general'
else :
    country = input()
    language = input()
    pageSize = input()  
    page = input()
    q = input()
    category = input()

cont = True
while(cont):
    print(
        'enter mode: '
        '1 - request'
        '2 - request category'
        '3 - request key wrd'
        )
    response = reqKeyW(country, TOKEN, pageSize, page, q)
    pprint.pprint(response.json())


