from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/horoscope')
def horoscope():
    return render_template('horoscope.html')

@app.route('/zodiac_sign')
def zodiac_sign():
    return render_template('zodiac_sign.html')

@app.route('/planets')
def planets():
    return render_template('planets.html')

@app.route('/soul')
def soul():
    return render_template('soul.html')

@app.route('/taro')
def taro():
    return render_template('taro.html')

if __name__ == '__main__':
    app.run(debug=True)
