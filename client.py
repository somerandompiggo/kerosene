import requests
import time

while(0 < 1):
    req = requests.get("http://127.0.0.1:5000")
    print(req.text)
    time.sleep(1)