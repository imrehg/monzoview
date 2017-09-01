#!/usr/bin/env python
from __future__ import division
import dothat.lcd as lcd
import dothat.backlight as backlight
import requests
import os

lcd.clear()

ACCOUNT_ID = os.getenv('ACCOUNT_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

def balanceshow():
    URL = "https://api.monzo.com/balance"
    payload = {'account_id': ACCOUNT_ID}
    headers = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}
    print(payload)
    r = requests.get(URL, params=payload, headers=headers)
    print(r)
    # if code is not 200...
    print(r.json())
    balance = r.json()
    backlight.rgb(160,0,0)
    lcd.set_cursor_position(0, 0)
    lcd.write("   ~ Monzo ~    ")
    lcd.set_cursor_position(0, 1)
    lcd.write("B: {b}{c}".format(b=balance['balance']/100, c=balance['currency']))
    lcd.set_cursor_position(0, 2)
    lcd.write("S: {s}{c}".format(s=balance['spend_today']/100, c=balance['currency']))

if __name__ == "__main__":
    if ACCOUNT_ID and ACCESS_TOKEN:
        balanceshow()
    else:
        print("No tokens!")
