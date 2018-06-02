from datetime import datetime, date, timedelta

now_datetime = datetime.now()
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
now_date = now_datetime.date()
# вчера
print(now_date - timedelta(days=1))
# сегодня
print(now_date) 
# месяц назад
now_date_d = now_date.day
pre_month_last_day_date = (now_date.replace(day=1) - timedelta(days=1))
while True:
    try:
        pre_month_date = pre_month_last_day_date.replace(day=now_date_d)
        break
    except ValueError:
        now_date_d -= 1
print(pre_month_date)
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime
datetime_from_str = datetime.strptime(
    "31/3/16 12:10:03.234567", '%d/%m/%y %H:%M:%S.%f')
