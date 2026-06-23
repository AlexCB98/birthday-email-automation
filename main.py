import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = 'email_1@gmail.com'
PASSWORD = 'Pass123(-)'


now = dt.datetime.now()
current_month = now.month
current_day   = now.day

data = pd.read_csv('birthdays.csv')

for index, row in data.iterrows():
    birthday_month = row['month']
    birthday_day = row['day']

    if birthday_month == current_month and birthday_day == current_day:

        random_letter = random.randint(1, 5)

        with open(f'letter_templates/letter_{random_letter}.txt') as letter_file:
            letter_content = letter_file.read()
            personalized_letter = letter_content.replace('[NAME]', row['name'])

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row['email'],
                msg=f'Subject: Happy Birthday, {row['name']}\n\n'
                    f'{personalized_letter}'
            )