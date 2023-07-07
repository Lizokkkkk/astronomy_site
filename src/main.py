from flask import Flask, render_template, request
from monthly_horoscope_generation import *
from divination_by_tarot_by_month import *
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/horoscope/')
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
    return render_template("horoscope.html", first=first, second=second, third=third)


@app.route('/tarot/')
def tarot():
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
