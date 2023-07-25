from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Визначаємо поточний день тижня
    current_date = datetime.now()
    current_weekday = current_date.weekday()  # 0 - понеділок, 6 - неділя

    # Знаходимо наступний понеділок
    next_monday = current_date + timedelta(days=(7 - current_weekday))
    # Визначаємо дату через тиждень
    next_week = next_monday + timedelta(days=7)

    # Створюємо словник для зберігання користувачів за днями тижня
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    # Додаємо користувачів до відповідних днів тижня
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # Якщо день народження входить в поточний тиждень, додаємо користувача в список
        if next_monday <= birthday < next_week:
            # Визначаємо день тижня дня народження
            weekday = birthday.strftime("%A")  # Форматуємо день народження в строку з днем тижня
            
            # Якщо день народження припадає на суботу або неділю, привітати в понеділок
            if weekday in ["Saturday", "Sunday"]:
                weekday = "Monday"
                
            birthdays_per_week[weekday].append(name)

    # Виводимо користувачів, яких потрібно привітати по днях
    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Приклад тестових даних
users = [
    {"name": "Bill", "birthday": datetime(2023, 7, 24)},
    {"name": "Jill", "birthday": datetime(2023, 7, 25)},
    {"name": "Kim", "birthday": datetime(2023, 7, 27)},
    {"name": "Jan", "birthday": datetime(2023, 7, 28)},
    {"name": "Alex", "birthday": datetime(2023, 7, 30)},
    {"name": "Emma", "birthday": datetime(2023, 7, 31)},
]

# Викликаємо функцію для тестових даних
get_birthdays_per_week(users)