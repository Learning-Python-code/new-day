import requests

url = 'http://jurnalotaku.com'
try:
    req = requests.get(url)
    if req.status_code == 200:
        print(f"Status code {req.status_code}")
        print(req.text)
    else:
        print("Yabai!!!")
except Exception as e:
    print(f"Bakayaro, error cok {e}")

print("END")
