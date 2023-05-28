import http.client
from environment import DB_ID, DB_API_KEY

conn = http.client.HTTPSConnection("apis.deutschebahn.com")

headers = {
    'DB-Client-Id': DB_ID,
    'DB-Api-Key': DB_API_KEY,
    'accept': "application/xml"
    }

conn.request("GET", "/db-api-marketplace/apis/timetables/v1/fchg/8000199", headers=headers)

res = conn.getresponse()
data = res.read()

result = data.decode("utf-8")

print(result)

# KIEL HBF: eva: 8000199 Kennung: AK