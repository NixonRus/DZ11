import requests

# res = requests.get('https://github.com/NixonRus')
# print(res)
# print(res.text)
# print(res.headers)
krit = {'q': 'cat', 'order': 'popular', 'min_width': '1000', 'min_height': '800'}
res = requests.get('https://ru.pinterest.com', params=krit)
print(res.url)
print(res.headers)
print(res)