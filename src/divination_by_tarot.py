import json
import random

def divination_by_tarot():
    # Чтение данных из файла tarot.json
    with open('tarot.json') as file:
        data = json.load(file)

    # Создание словаря tarot_by_month
    tarot_by_month = {
        "Январь": None,
        "Февраль": None,
        "Март": None,
        "Апрель": None,
        "Май": None,
        "Июнь": None,
        "Июль": None,
        "Август": None,
        "Сентябрь": None,
        "Октябрь": None,
        "Ноябрь": None,
        "Декабрь": None
    }

    # Генерация комбинаций для каждого месяца
    for month in tarot_by_month:
        # Словарь для хранения объектов месяца
        month_objects = {}

        # Выбор трех случайных объектов без повторений
        random_objects = random.sample(data, 3)

        # Добавление объектов в словарь month_objects
        for obj in random_objects:
            name = obj['name']
            positions = ['direct position', 'inverted position']
            position = random.choice(positions)
            month_objects[name] = obj[f'{position}']

        # Присвоение словаря month_objects соответствующему месяцу
        tarot_by_month[month] = month_objects

    # Вывод результатов
    for month, objects in tarot_by_month.items():
        print(month + ":")
        for name, position in objects.items():
            print(f"  {name}: {position}")


# divination_by_tarot()
