import random
import datetime

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

zodiac_signs = {
    "Водолей": None,
    "Рыбы": None,
    "Овен": None,
    "Телец": None,
    "Близнецы": None,
    "Рак": None,
    "Лев": None,
    "Дева": None,
    "Весы": None,
    "Скорпион": None,
    "Стрелец": None,
    "Козерог": None
}


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


def generate_horoscope():
    first_horoscope = random.choice(first)
    second_horoscope = random.choice(second)
    second_add_horoscope = random.choice(second_add)
    third_horoscope = random.choice(third)
    return f"{first_horoscope} {second_horoscope} {second_add_horoscope} {third_horoscope}"


def get_horoscope(zodiac_sign):
    current_date = datetime.date.today().strftime("%d-%m-%Y")

    if zodiac_signs[zodiac_sign] is None or zodiac_signs[zodiac_sign][0] != current_date:
        horoscope = generate_horoscope()
        zodiac_signs[zodiac_sign] = (current_date, horoscope)
    else:
        horoscope = zodiac_signs[zodiac_sign][1]

    return horoscope


print('Добро пожаловать на наш сайт с гороскопом! Здесь вы найдете '
      'уникальные и точные предсказания, которые помогут вам раскрыть '
      'потенциал каждого дня. Позвольте звездам провести вас сквозь жизненные '
      'вызовы и откройте двери к новым возможностям с нашими подробными гороскопами.')

name = input('Как Вас зовут? ')
month = int(input(f"{name}, пожалуйста введите месяц вашего рождения (числом): "))
day = int(input("Введите день вашего рождения: "))

sign = determine_zodiac_sign(month, day)
print(f"Ваш знак зодиака - {sign}. Вот ваш прогноз на сегодня:")

horoscope = get_horoscope(sign)

print(horoscope)
