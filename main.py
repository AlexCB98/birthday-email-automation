import pandas as pd
import datetime as dt
import smtplib
import random

now = dt.datetime.now()

month = now.month
day   = now.day

data = pd.read_csv('birthdays.csv')

for index, row in data.iterrows():
    month = row.month
    day = row.day
    name = row.name
    print(f'Name: {row['name']} | Day: {day} | Month: {month}')

