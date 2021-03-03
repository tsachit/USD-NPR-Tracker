# USD-Tracker

Just a simple tracker from **Transferwise** to fetch USD to NPR rate in every 5 minutes.

### Setup
Note: Only if you want to use venv
```
> python -m venv venv
> source venv/bin/activate
```

install all the dependency using this
```
pip install -r requirements.txt
```

Change interval value in `tracker.py` to increase/decrease the frequency.

### How to run
If you're using venv then activate it
```
source venv/bin/activate
```
and run tracker command
```
python tracker.py
```

If you also want alert on above threshold value, try running like this

```
python tracker.py 117
```
This will send you push notification if USD-NPR rate is above Rs.117