import pandas as pd
import datetime as dt
import smtplib
import random

now = dt.datetime.now()
current_month = now.month
current_day   = now.day

data = pd.read_csv('birthdays.csv')

my_email = 'email_1@gmail.com'
password = 'Pass123(-)'


for index, row in data.iterrows():
    birthday_month = row.month
    birthday_day = row.day

    random_letter = random.randint(1, 5)

    with open(f'letter_templates/letter_{random_letter}.txt') as letter_file:
        letter_content = letter_file.read()
        personalized_letter = letter_content.replace('[NAME]', row['name'])


    if birthday_month == current_month and birthday_day == current_day:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='email_2@gmail.com',
                msg=f'Subject: Happy Birthday, {row['name']}\n\n'
                    f'{personalized_letter}'
            )