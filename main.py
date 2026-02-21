import requests
from send_email import send_email
api_key = "1abb172f46224091956d2b49ef0da16a"
url = ('https://newsapi.org/v2/everything?q=apple&from'
       '=2026-02-20&to=2026-02-20&sortBy=popularity&apiKey=') + api_key
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
code = response.status_code
content = response.json()
#print(code)
#print(type(content))
print(content)

article = content["articles"][0]

title = article.get("title", "No title")
description = article.get("description", "")

body = f"{title}\n{description}\n\n"
send_email(body)
for item in content['articles']:
    body += item['title'] + '\n' + item['description'] + 2*'\n'

'''response = requests.get(url)
text = response.text
print(text)'''