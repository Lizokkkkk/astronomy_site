import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="stars",
                        user="postgres",
                        password=" ",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/horoscope/', methods=['POST', 'GET'])
def subscription():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        surname = request.form.get('surname')
        date = request.form.get('date')
        bday = date[0:1]
        bmonth = date[3:4]
        id = request.form.get('id')

        if not first_name or not surname or not date or not id:
            return render_template('horoscope.html', error="Пожалуйста, заполните все поля")

        cursor.execute('SELECT 1 FROM user_info WHERE first_name=%s AND surname=%s AND bday=%s AND '
                       'bmonth=%s AND id=%s LIMIT 1', (str(first_name), str(surname), int(bday), int(bmonth), int(id)))
        if cursor.fetchone():
            return render_template('horoscope.html', error="Вы уже подписаны на рассылку")

        cursor.execute('INSERT INTO user_info (first_name, surname, bday, bmonth, id) VALUES (%s, %s, %s, %s, %s);',
                       (str(first_name), str(surname), int(bday), int(bmonth), int(id)))
        conn.commit()

    return render_template('horoscope.html')
