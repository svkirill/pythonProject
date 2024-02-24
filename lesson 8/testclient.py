import http.client
import ssl
from datetime import datetime, timezone
import json

# создаем объект HTTPSConnection, это такая сущность, через которую
# мы можем отправлять различные запросы на серваки
# плюс его использования - ты указываешь адрес сервера, порт
# и можешь использовать один и тот же объект для отправки любых запросов на этот же самый сервер.
conn = http.client.HTTPSConnection("ngw.devices.sberbank.ru", 9443, context=ssl._create_unverified_context()) # ssl... - чтобы не валидировать сертификата, говорим, что доверяем серверу

# body (тело запроса)
payload = 'scope=SALUTE_SPEECH_PERS'

# заголовки
headers = {
  'RqUID': '6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic MTY4ZGQwNTMtYzViNS00MWQ4LTgyNzMtZDlkMTk2MTNjMDgzOmQ3MGVmOGEwLTJiMmYtNGNjMS1iMDI5LTJhMzk1NjU0ZDEzZg=='
}

# отправляем запрос на /api/v2/outh, прикрепляем заголовки, тело запроса
# POST - отправляем данные
# GET - получаем
# DELETE - удаляем
# UPDATE - обновляем (сейчас вместо него используют POST)
conn.request("POST", "/api/v2/oauth", payload, headers)

# получаем объект ответа
res = conn.getresponse()
print(res.getcode())

# читаем тело ответа в кодировке utf-8
strData = res.read().decode('utf-8')

# через json подгружаем данные, передаем туда текст, получаем словарь
# : dict - явно указываем тип данных, чтобы были подсказки в pycharm
data: dict = json.loads(strData)

# Получаем данные из словаря
exp = data.get("expires_at")
token = data.get("access_token")
#with open("filePath.mp3", "r") as file:
#  payload = file.read()
print(exp)
print(datetime.fromtimestamp(exp//1000, timezone.utc))

print(token)


# 1970.02.02 12:00:00.0000000
# 2024.02.02 12:45:53.9900000