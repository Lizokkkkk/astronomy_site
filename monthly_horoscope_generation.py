import datetime
import random


# Списки предложений для каждой части гороскопа
first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про",
          "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

# Словарь, хранящий знаки зодиака и соответствующие гороскопы
zodiac_signs = {
    "January": {"signs": [], "horoscopes": []},
    "February": {"signs": [], "horoscopes": []},
    "March": {"signs": [], "horoscopes": []},
    "April": {"signs": [], "horoscopes": []},
    "May": {"signs": [], "horoscopes": []},
    "June": {"signs": [], "horoscopes": []},
    "July": {"signs": [], "horoscopes": []},
    "August": {"signs": [], "horoscopes": []},
    "September": {"signs": [], "horoscopes": []},
    "October": {"signs": [], "horoscopes": []},
    "November": {"signs": [], "horoscopes": []},
    "December": {"signs": [], "horoscopes": []}
}


# Определение знака зодиака на основе месяца и дня рождения
def determine_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Стрелец"
    else:
        zodiac_sign = "Козерог"

    return zodiac_sign


# Генерация случайного гороскопа
def generate_horoscope():
    first_horoscope = random.choice(first)
    second_horoscope = random.choice(second)
    second_add_horoscope = random.choice(second_add)
    third_horoscope = random.choice(third)
    return f"{first_horoscope} {second_horoscope} {second_add_horoscope} {third_horoscope}"


# Обновление словаря zodiac_signs для текущего месяца
def update_zodiac_signs():
    current_month = datetime.datetime.now().strftime("%B")  # Получаем текущий месяц в формате полного названия (например, "June")
    zodiac_signs[current_month]["signs"] = []  # Очищаем список знаков зодиака
    zodiac_signs[current_month]["horoscopes"] = []  # Очищаем список гороскопов

    for _ in range(12):
        zodiac_sign = random.choice(list(zodiac_signs.keys()))  # Случайный выбор знака зодиака
        horoscope = generate_horoscope()  # Генерация случайного гороскопа
        zodiac_signs[current_month]["signs"].append(zodiac_sign)  # Добавляем знак зодиака в список
        zodiac_signs[current_month]["horoscopes"].append(horoscope)  # Добавляем гороскоп в список


# Получение гороскопа для знака зодиака
def get_horoscope(zodiac_sign):
    current_month = datetime.datetime.now().strftime("%B")  # Получаем текущий месяц в формате полного названия (например, "June")
    signs = zodiac_signs[current_month]["signs"]
    horoscopes = zodiac_signs[current_month]["horoscopes"]

    if zodiac_sign in signs:
        index = signs.index(zodiac_sign)  # Индекс знака зодиака в списке
        horoscope = horoscopes[index]  # Получаем гороскоп по индексу
    else:
        horoscope = generate_horoscope()  # Генерируем новый гороскоп
        zodiac_signs[current_month]["signs"].append(zodiac_sign)  # Добавляем знак зодиака в список
        zodiac_signs[current_month]["horoscopes"].append(horoscope)  # Добавляем гороскоп в список

    return horoscope


# Основная функция
def main():
    current_month = datetime.datetime.now().strftime("%B")  # Получаем текущий месяц в формате полного названия (например, "June")
    if not zodiac_signs[current_month]["signs"] or not zodiac_signs[current_month]["horoscopes"]:
        update_zodiac_signs()  # Обновляем словарь zodiac_signs для текущего месяца

    month = int(input("Введите номер месяца вашего рождения: "))
    day = int(input("Введите число вашего рождения: "))
    zodiac_sign = determine_zodiac_sign(month, day)
    horoscope = get_horoscope(zodiac_sign)
    print(f"Ваш знак зодиака: {zodiac_sign}")
    print(f"Ваш гороскоп на текущий месяц: {horoscope}")


# Вызов основной функции
if __name__ == "__main__":
    main()
