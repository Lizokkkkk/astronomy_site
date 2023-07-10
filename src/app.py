from flask import Flask, render_template, request
from monthly_horoscope_generation import *
from divination_by_tarot_by_month import divination_by_tarot, update_tarot_predictions
from number_of_path import calculation
import datetime
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="stars",
                        user="postgres",
                        password=" ",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

# Переменная для хранения даты последнего обновления
last_update_date = None


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/horoscope/', methods=['POST', 'GET'])
def horoscope():
    current_month = datetime.datetime.now().strftime("%B")
    if not zodiac_signs[current_month]["signs"] or not zodiac_signs[current_month]["horoscopes"]:
        update_zodiac_signs()
    sign = request.args.get('sign')
    horoscope_output = get_horoscope(sign)
    forecast = horoscope_output.split('.')
    first = forecast[0] + '.'
    second = forecast[1] + forecast[2] + '.'
    third = forecast[3] + '.'

    # для подписки
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        surname = request.form.get('surname')
        date = request.form.get('date')
        bday = int(date[0:2])
        bmonth = int(date[3:5])
        zodiac_sign = request.args.get('sign')
        id = request.form.get('vk_id')

        if not first_name or not surname or not date or not id:
            return render_template('horoscope.html', first=first, second=second, third=third,
                                   error="Пожалуйста, заполните все поля")

        cursor.execute('SELECT 1 FROM user_info WHERE vk_id=' + str(id) + ' LIMIT 1')
        if cursor.fetchone():
            return render_template('horoscope.html', first=first, second=second, third=third,
                                   error="Вы уже подписаны на рассылку")

        cursor.execute(
            'INSERT INTO user_info (first_name, surname, bday, bmonth, zodiac_sign, vk_id) VALUES (%s, %s, %s, %s, %s, %s);',
            (str(first_name), str(surname), int(bday), int(bmonth), str(zodiac_sign), int(id)))
        conn.commit()
        return render_template('horoscope.html', first=first, second=second, third=third,
                               confirmation="Поздравляем! Вы подписались на рассылку")

    return render_template("horoscope.html", first=first, second=second, third=third)


@app.route('/tarot/')
def tarot():
    global last_update_date

    # Проверяем, нужно ли обновлять словарь tarot_by_month
    current_date = datetime.datetime.now()
    if last_update_date is None or (current_date.weekday() == 0 and current_date.date() > last_update_date.date()):
        update_tarot_predictions()
        # Обновляем дату последнего обновления
        last_update_date = current_date

    sign = request.args.get('sign')
    tarot_output = divination_by_tarot(sign)

    card_name_1 = tarot_output[0]['name']
    card_name_2 = tarot_output[1]['name']
    card_name_3 = tarot_output[2]['name']
    card_image_1 = tarot_output[0]['image']
    card_image_2 = tarot_output[1]['image']
    card_image_3 = tarot_output[2]['image']
    card_interpretation_1 = tarot_output[0]['interpretation']
    card_interpretation_2 = tarot_output[1]['interpretation']
    card_interpretation_3 = tarot_output[2]['interpretation']

    return render_template("tarot.html", card_name_1=card_name_1, card_name_2=card_name_2, card_name_3=card_name_3,
                           card_image_1=card_image_1, card_image_2=card_image_2, card_image_3=card_image_3,
                           card_interpretation_1=card_interpretation_1, card_interpretation_2=card_interpretation_2,
                           card_interpretation_3=card_interpretation_3)


@app.route('/sign/')
def sign():
    sign = request.args.get('sign')
    return render_template("sign.html")


@app.route('/planet/')
def planet():
    sign = request.args.get('sign')
    return render_template("planet.html")


@app.route('/numerology/')
def numerology():
    date = request.args.get('date')
    paragraphs = calculation(date).split('\n\n')
    number = int(paragraphs[0])
    first_paragraph = paragraphs[1]
    second_paragraph = paragraphs[2]
    return render_template("numerology.html", number=number, first_paragraph=first_paragraph, second_paragraph=second_paragraph)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
