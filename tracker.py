import requests
import sched, time
from datetime import datetime

# run interval in seconds
interval = 300

def get_rate():
    url = "https://api.transferwise.com/v3/comparisons?sourceCurrency=USD&targetCurrency=NPR&sendAmount=1"
    response = requests.request("GET", url, headers={}, data={})
    json_resp = response.json()
    return json_resp['providers'][0]['quotes'][0]['rate']


print("*********************************************************")
print("*\t\tFetching currency rate...\t\t*")
print("*********************************************************")
# do your stuff
print("Time \t\t\t\t\t Rate")
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \t\t\t ${get_rate()}")
    s.enter(interval, 1, do_something, (sc,))

# run instantly
s.enter(0, 1, do_something, (s,))
s.run()