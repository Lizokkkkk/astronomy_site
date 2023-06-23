import json
import random   # ПРОГРАММА ВЫДАЕТ ПРОГНОЗ ПО НОМЕРУ МЕСЯЦА, А ТАКЖЕ ВЫДАЕТ В КАКОМ ПОЛОЖЕНИИ ВЫПАЛА КАРТА (ПРЯМОМ ИЛИ ПЕРЕВЕРНУТОМ)


def divination_by_tarot():
    # Чтение данных из файла tarot.json
    with open('tarot.json') as file:
        data = json.load(file)

    # Создание словаря tarot_by_month
    tarot_by_month = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
    }

    # Генерация комбинаций для каждого месяца
    for month_number, month_name in tarot_by_month.items():
        # Словарь для хранения объектов месяца
        month_objects = {}

        # Выбор трех случайных объектов без повторений
        random_objects = random.sample(data, 3)

        # Добавление объектов в словарь month_objects
        for obj in random_objects:
            name = obj['name']
            positions = ['direct position', 'inverted position']
            position = random.choice(positions)
            if position == 'direct position':
                month_objects[name] = obj[f'{position}'], 'direct img'
            else:
                month_objects[name] = obj[f'{position}'], 'inverted img'

        # Присвоение словаря month_objects соответствующему месяцу
        tarot_by_month[month_number] = month_objects

    # Запрос номера месяца рождения
    birth_month = int(input("Введите номер месяца вашего рождения (от 1 до 12): "))

    # Проверка введенного номера месяца
    if birth_month in tarot_by_month:
        selected_month = tarot_by_month[birth_month]

        # Вывод результатов выбранного месяца
        print("Результаты для выбранного месяца:")
        for name, position in selected_month.items():
            print(f"  {name}: {position}")
    else:
        print("Некорректный номер месяца.")


divination_by_tarot()
