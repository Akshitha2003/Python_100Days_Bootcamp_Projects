import pandas
import random
import smtplib
import datetime as dt

# 1. Update the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")
birthday_data_dict = birthday_data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_day = now.day
today_month = now.month

birthday_baby_name = ""
birthday_baby_email = ""
for detail in birthday_data_dict:
    if today_day == detail["day"] and today_month == detail["month"]:
        birthday_baby_name = detail["name"]
        birthday_baby_email = detail["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
if birthday_baby_name != "":
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_template:
        text = letter_template.read()
    text = text.replace("[NAME]", birthday_baby_name)

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="testuser1udemy@gmail.com", password="ccnwwannsltwuxsp")
        connection.sendmail(from_addr="testuser1udemy@gmail.com",
                            to_addrs=birthday_baby_email,
                            msg=f"Subject:Happy Birthday!!!\n\n{text}"
                            )
