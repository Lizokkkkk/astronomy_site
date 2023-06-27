import datetime
import random
from flask import Flask, render_template, request
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

# Списки предложений для каждой части гороскопа
first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про.",
          "Если поедете за город, заранее подумайте про.",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про.",
          "Если у вас упадок сил, обратите внимание на.",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про."]

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


# Генерация случайного гороскопа
def generate_horoscope():
    first_horoscope = random.choice(first)
    second_horoscope = random.choice(second)
    second_add_horoscope = random.choice(second_add)
    third_horoscope = random.choice(third)
    return f"{first_horoscope} {second_horoscope} {second_add_horoscope} {third_horoscope}"


# Обновление словаря zodiac_signs для текущего месяца
def update_zodiac_signs():
    current_month = datetime.datetime.now().strftime("%B")
    zodiac_signs[current_month]["signs"] = []
    zodiac_signs[current_month]["horoscopes"] = []

    for _ in range(12):
        zodiac_sign = random.choice(list(zodiac_signs.keys()))
        horoscope = generate_horoscope()
        zodiac_signs[current_month]["signs"].append(zodiac_sign)
        zodiac_signs[current_month]["horoscopes"].append(horoscope)


# Получение гороскопа для знака зодиака
def get_horoscope(zodiac_sign):
    current_month = datetime.datetime.now().strftime("%B")
    signs = zodiac_signs[current_month]["signs"]
    horoscopes = zodiac_signs[current_month]["horoscopes"]

    if zodiac_sign in signs:
        index = signs.index(zodiac_sign)
        horoscope = horoscopes[index]
    else:
        horoscope = generate_horoscope()
        zodiac_signs[current_month]["signs"].append(zodiac_sign)
        zodiac_signs[current_month]["horoscopes"].append(horoscope)

    return horoscope

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign/')
def sign():
    sign = request.args.get('sign')
    return render_template("sign.html")

@app.route('/planet/')
def planet():
    sign = request.args.get('sign')
    return render_template("planet.html")

# Основная функция
@app.route('/horoscope/')
def horoscope():
    current_month = datetime.datetime.now().strftime("%B")
    if not zodiac_signs[current_month]["signs"] or not zodiac_signs[current_month]["horoscopes"]:
        update_zodiac_signs()

    # Получение значения параметра 'sign' из запроса
    zodiac_sign = request.args.get('sign')

    if zodiac_sign is None:
        # Здесь можно вернуть ошибку или предоставить значение по умолчанию
        return "Знак зодиака не указан"

    horoscope = get_horoscope(zodiac_sign)
    new_horoscope = horoscope.split('.')
    # print(f"Ваш знак зодиака: {zodiac_sign}")
    first_sent = new_horoscope[0] + '.'
    second_sent = new_horoscope[1] + new_horoscope[2] + '.'
    third_sent = new_horoscope[3] + '.'
    return render_template('horoscope.html', first=first_sent, second=second_sent,
                           third=third_sent)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)