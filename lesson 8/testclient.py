import http.client
import ssl
from datetime import datetime, timezone
import json

conn = http.client.HTTPSConnection("ngw.devices.sberbank.ru", 9443, context=ssl._create_unverified_context())
payload = 'scope=SALUTE_SPEECH_PERS'
headers = {
  'RqUID': '6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic MTY4ZGQwNTMtYzViNS00MWQ4LTgyNzMtZDlkMTk2MTNjMDgzOmQ3MGVmOGEwLTJiMmYtNGNjMS1iMDI5LTJhMzk1NjU0ZDEzZg=='
}
conn.request("POST", "/api/v2/oauth", payload, headers)
res = conn.getresponse()
print(res.getcode())
strData = res.read().decode('utf-8')
data: dict = json.loads(strData)
exp = data.get("expires_at")
token = data.get("access_token")
#with open("filePath.mp3", "r") as file:
#  payload = file.read()
print(exp)

print(datetime.fromtimestamp(exp//1000, timezone.utc))

print(token)


# 1970.02.02 12:00:00.0000000
# 2024.02.02 12:45:53.9900000