from datetime import datetime, date


def calc_age(birthday):
    birthday = datetime.strptime(birthday, "%d-%m-%Y").date()
    today = date.today()
    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age


print(calc_age("05-12-2001"))
