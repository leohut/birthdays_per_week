from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # Визначимо дні тижня відповідно до індексів
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Отримаємо поточний день тижня (0 - понеділок, 6 - неділя)
    current_day_of_week = datetime.today().weekday()

    # Створимо пустий словник для збереження іменинників за днями тижня
    birthdays_per_week = {
          "Monday": [],
          "Tuesday": [],
          "Wednesday": [],
          "Thursday": [],
          "Friday": [],
          "Saturday": [],
          "Sunday": []
         }

    # Пройдемося по списку користувачів і додамо їх до відповідного дня тижня у словник
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # Визначимо день народження на поточному тижні (залишивши рік незмінним)
        this_year_birthday = birthday.replace(year=datetime.today().year)

        # Визначимо день тижня для дня народження
        birthday_day_of_week = this_year_birthday.weekday()

        # Визначимо день тижня ПОНЕДІЛОК
        monday = current_day_of_week - current_day_of_week % 7

        # Знайдемо відстань між поточним днем тижня та днем народження
        days_to_birthday = (birthday_day_of_week - monday) % 7

        # Якщо день народження вже був на цьому тижні і припадає на суботу або неділю,
        # перенесемо його на наступний тиждень
        
        # if birthday_day_of_week in ["Saturday", "Sunday"]:
        #           days_to_birthday = "Monday"
        
        if birthday_day_of_week == 0 and birthday_day_of_week >= 5:
            birthday_day_of_week = 7

        # Додамо користувача до списку відповідного дня тижня
        birthdays_per_week[days_of_week[(current_day_of_week + days_to_birthday) % 7]].append(name)

    # Виведемо іменинників у консоль
    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Приклад тестових даних
users = [
    {"name": "Bill", "birthday": datetime(2000, 8, 30)}, # неділя
    {"name": "Jill", "birthday": datetime(1995, 8, 15)}, # субота
    {"name": "Kim", "birthday": datetime(1987, 8, 8)},  # субота
    {"name": "Jan", "birthday": datetime(1992, 8, 19)},  # середа
    {"name": "John", "birthday": datetime(1964, 8, 27)},  # четвер
    {"name": "Mikhael", "birthday": datetime(1998, 8, 16)},  # неділя
]

get_birthdays_per_week(users)