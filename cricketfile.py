import requests
url = 'https://api.covid19api.com/summary'

res = requests.get(url)
print(res.text)
