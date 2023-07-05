from flask import Flask, render_template, request
from monthly_horoscope_generation import get_horoscope
import divination_by_tarot_by_month

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/horoscope/')
def horoscope():
    sign = request.args.get('sign')
    horoscope_output = get_horoscope(sign)
    forecast = horoscope_output.split('.')
    first = forecast[0]
    second = forecast[1]
    third = forecast[2]
    return render_template("horoscope.html", first=first, second=second, third=third)


@app.route('/tarot/')
def tarot():
    sign = request.args.get('sign')
    tarot_output = divination_by_tarot_by_month.get_tarot(sign)
    return render_template("tarot.html", tarot_output=tarot_output)


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
