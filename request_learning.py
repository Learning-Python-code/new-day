import requests

url = 'http://jurnalotaku.com'
try:
    req = requests.get(url)
    if req.status_code == 200:
        print(f"JOI Status code {req.status_code}")
        print(req.text)
    else:
        print("Yabai JOI error!!!")
except Exception as e:
    print(f"Bakayaro, JOI not found. Error : {e}")

print("END")
