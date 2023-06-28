from flask import Flask, render_template, request
from monthly_horoscope_generation import get_horoscope

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
    second =  forecast[1]
    third = forecast[2]
    return render_template("horoscope.html", first=first, second=second, third=third)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
