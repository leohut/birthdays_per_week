from datetime import datetime, timedelta

def get_birthdays_per_week(users):
       
    birthdays_by_weekday = {i: [] for i in range(7)}  # Створюємо словник для зберігання іменинників на кожний день тижня.
    for user in users:
        birthday = user["birthday"].date() # Отримуємо день народження користувача з об'єкту datetime.
        birthday_day_of_week = birthday.weekday() # Визначаємо день тижня, на який припадає день народження (понеділок - 0, неділя - 6).
        
        if birthday_day_of_week >= 5:  # Перевіряємо, чи є день тижня вихідним (субота або неділя). 5 і 6 - вихідні дні (субота, неділя).            
            days_to_add = 2 if birthday_day_of_week == 5 else 1 # Знаходимо, скільки днів потрібно додати до дня народження, щоб перенести його.            
            birthday = birthday + timedelta(days=days_to_add) # Знаходимо новий день для привітання.
        
        birthdays_by_weekday[birthday.weekday()].append(user["name"]) # Додаємо ім'я користувача до списку іменинників на відповідний день тижня.
    
    for i in range(7):   # Виводимо іменинників
        day_name = datetime(2000, 1, 3 + i).strftime('%A')  
        if birthdays_by_weekday[i]:
            print(f"{day_name}: {', '.join(birthdays_by_weekday[i])}")
            
            
# тестовий список users:
users = [
    {"name": "Alex", "birthday": datetime(2023, 7, 25)}, #вівторок
    {"name": "Eva", "birthday": datetime(2022, 1, 2)}, #неділя
    {"name": "Mikhael", "birthday": datetime(2022, 1, 1)}, #суббота
    {"name": "John", "birthday": datetime(2023, 7, 27)},  # Четвер
    {"name": "Mike", "birthday": datetime(2023, 7, 28)},  # П'ятниця
    {"name": "Bill", "birthday": datetime(2023, 7, 30)},  # Неділя
    {"name": "Enrique", "birthday": datetime(2023, 7, 26)},   #середа
]
get_birthdays_per_week(users)