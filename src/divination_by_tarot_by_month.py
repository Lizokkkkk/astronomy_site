import json
import random
import datetime
import os

tarot_by_month = {
    "Овен": {'cards': {}, 'updated_date': None},
    "Телец": {'cards': {}, 'updated_date': None},
    "Близнецы": {'cards': {}, 'updated_date': None},
    "Рак": {'cards': {}, 'updated_date': None},
    "Лев": {'cards': {}, 'updated_date': None},
    "Дева": {'cards': {}, 'updated_date': None},
    "Весы": {'cards': {}, 'updated_date': None},
    "Скорпион": {'cards': {}, 'updated_date': None},
    "Стрелец": {'cards': {}, 'updated_date': None},
    "Козерог": {'cards': {}, 'updated_date': None},
    "Водолей": {'cards': {}, 'updated_date': None},
    "Рыбы": {'cards': {}, 'updated_date': None}
}


def update_tarot_predictions():
    global tarot_by_month

    # Проверяем, когда были последние обновления
    today = datetime.date.today()
    for zodiac_sign, predictions in tarot_by_month.items():
        updated_date = predictions.get('updated_date')
        if updated_date is None or (today - updated_date).days >= 7:
            # Обновляем предсказания
            updated_predictions = generate_tarot_predictions()
            predictions['cards'] = updated_predictions
            predictions['updated_date'] = today


def generate_tarot_predictions():
    # Определяем путь к файлу tarot.json
    current_directory = os.path.dirname(os.path.abspath(__file__))
    tarot_file_path = os.path.join(current_directory, 'static', 'json', 'tarot.json')

    # Читаем данные из файла tarot.json
    with open(tarot_file_path, encoding="utf8") as file:
        data = json.load(file)

    # Генерируем три случайные карты
    random_cards = random.sample(data, 3)

    # Список для хранения предсказаний трех карт
    tarot_predictions = []

    for obj in random_cards:
        name = obj['name']
        positions = ['direct position', 'inverted position']
        position = random.choice(positions)
        if position == 'direct position':
            tarot_predictions.append({
                'image': obj['direct img'],
                'name': name,
                'interpretation': obj[f'{position}']
            })
        else:
            tarot_predictions.append({
                'image': obj['direct img'],
                'name': name,
                'interpretation': obj[f'{position}']
            })

    return tarot_predictions


def divination_by_tarot(sign):
    global tarot_by_month

    # Обновляем предсказания, если требуется
    update_tarot_predictions()

    # Проверяем введенный знак зодиака
    if sign in tarot_by_month:
        selected_sign = tarot_by_month[sign]
        tarot_output = selected_sign['cards']
    else:
        tarot_output = []

    return tarot_output
