debug = True

import requests, pprint

def reqwCat(mode, country, category, TOKEN, pageSize, page):
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
    f'country={country}&'
    f'category={category}&'
    f'pageSize={pageSize}&'
    f'page = {page}&'
    f'apiKey = {TOKEN}'
    ) 

def reqwKeyW(mode, q, country, TOKEN, pageSize, page):
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
    f'q={q}&'
    f'country={country}&'
    f'pageSize={pageSize}&'
    f'page = {page}&'
    f'apiKey = {TOKEN}'
    ) 

def reqw(mode, county, pageSize, page, TOKEN):
    return requests.get(
    f'https://newsapi.org/v2/{mode}?'
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
