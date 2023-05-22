import http.client

conn = http.client.HTTPSConnection("apis.deutschebahn.com")

headers = {
    'DB-Client-Id': "e3f1f5b7404f3d29525d455264cc0919",
    'DB-Api-Key': "0f0e551988852973d4b7642736b1fb5f",
    'accept': "application/xml"
    }

conn.request("GET", "/db-api-marketplace/apis/timetables/v1/fchg/8000199", headers=headers)

res = conn.getresponse()
data = res.read()

result = data.decode("utf-8")


# KIEL HBF: eva: 8000199 Kennung: AK