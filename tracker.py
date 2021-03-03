import requests
import sys
import sched, time
from datetime import datetime
from notifypy import Notify

# run interval in seconds
interval = 300
url = "https://api.transferwise.com/v3/comparisons?sourceCurrency=USD&targetCurrency=NPR&sendAmount=1"

notification = Notify(
  default_notification_title="USD-NPR Tracker",
  default_notification_icon="./assets/logo.png",
  default_notification_audio="./assets/sound.wav"
)

def notify(rate):
    if(len(sys.argv) > 1):
        threshold = float(sys.argv[1])
        if(rate > threshold):
            notification.message = f"USD to NPR rate is now Rs.{rate}, i.e. above the limit Rs.{threshold}"
            notification.send()

def get_rate():
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
    rate = get_rate()
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \t\t\t Rs.{rate}")
    notify(rate)
    s.enter(interval, 1, do_something, (sc,))

# run instantly
s.enter(0, 1, do_something, (s,))
s.run()