a = lambda x:x**2

print((a(10)))

b = lambda y,u:y+u

print(b(2,3))


c = lambda x,b: x**2 + b**4

print((c(2,3)))

import requests
#link= 'https://icanhazip.com/'
#print(requests.get(link).text)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
link = 'https://httpbin.org/post'

data = {'custname': 'elton john',
        'custtel': '7978000000',
        'custemail': 'elton@mail.ru',
        'size': 'large',
        'topping': 'onion',
        'delivery': '21:00',
        'comments': 'hi' }

print(requests.post(url=link, headers=headers, params=data).text)

