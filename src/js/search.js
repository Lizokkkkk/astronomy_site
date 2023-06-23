search_input.max = new Date().toISOString().split("T")[0];

const data = document.getElementById('search_input'),
      btn_horoscope = document.getElementById('search_btn1'),
      btn_sign = document.getElementById('search_btn2'),
      btn_planet = document.getElementById('search_btn3'),
      btn_numerology = document.getElementById('search_btn4'),
      btn_tarot = document.getElementById('search_btn5');
      
btn_sign.addEventListener("click", () => {
    birthdate = new Date(data.value);
    const month = birthdate.getMonth() + 1;
    const day = birthdate.getDate();
    switch (month) {
        case 1:
            if (day <= 20)
                sign = 'Козерог';
            else
                sign = 'Водолей';
            break;
        case 2:
            if (day <= 18)
                sign = 'Водолей';
            else
                sign = 'Рыбы';
            break;
        case 3:
            if (day <= 20)
                sign = 'Рыбы';
            else
                sign = 'Овен';
            break;
        case 4:
            if (day <= 20)
                sign = 'Овен';
            else
                sign = 'Телец';
            break;
        case 5:
            if (day <= 20)
                sign = 'Телец';
            else
                sign = 'Близнецы';
            break;
        case 6:
            if (day <= 21)
                sign = 'Близнецы';
            else
                sign = 'Рак';
            break;
        case 7:
            if (day <= 22)
                sign = 'Рак';
            else
                sign = 'Лев';
            break;
        case 8:
            if (day <= 22)
                sign = 'Лев';
            else
                sign = 'Дева';
            break;
        case 9:
            if (day <= 23)
                sign = 'Дева';
            else
                sign = 'Весы';
            break;
        case 10:
            if (day <= 23)
                sign = 'Весы';
            else
                sign = 'Скорпион';
            break;
        case 11:
            if (day <= 22)
                sign = 'Скорпион';
            else
                sign = 'Стрелец';
            break;
        case 12:
            if (day <= 21)
                sign = 'Стрелец';
            else
                sign = 'Козерог';
            break;
    }
    location.href = `https://lizokkkkk.github.io/astronomy_site//src/html/sign.html?sign=${sign}`;
});

btn_planet.addEventListener("click", () => {
    birthdate = new Date(data.value);
    const month = birthdate.getMonth() + 1;
    const day = birthdate.getDate();
    switch (month) {
        case 1:
            if (day <= 20)
                planet = 'Сатурн';
            else
                planet = 'Уран';
            break;
        case 2:
            if (day <= 18)
                planet = 'Уран';
            else
                planet = 'Плутон';
            break;
        case 3:
            if (day <= 20)
                planet = 'Плутон';
            else
                planet = 'Марс';
            break;
        case 4:
            if (day <= 20)
                planet = 'Марс';
            else
                planet = 'Венера';
            break;
        case 5:
            if (day <= 20)
                planet = 'Венера';
            else
                planet = 'Меркурий';
            break;
        case 6:
            if (day <= 21)
                planet = 'Меркурий';
            else
                planet = 'Луна';
            break;
        case 7:
            if (day <= 22)
                planet = 'Луна';
            else
                planet = 'Солнце';
            break;
        case 8:
            if (day <= 22)
                planet = 'Солнце';
            else
                planet = 'Нептун';
            break;
        case 9:
            if (day <= 23)
                planet = 'Нептун';
            else
                planet = 'Венера';
            break;
        case 10:
            if (day <= 23)
                planet = 'Венера';
            else
                planet = 'Плутон';
            break;
        case 11:
            if (day <= 22)
                planet = 'Плутон';
            else
                planet = 'Юпитер';
            break;
        case 12:
            if (day <= 21)
                planet = 'Юпитер';
            else
                planet = 'Сатурн';
            break;
    }
    location.href = `https://lizokkkkk.github.io/astronomy_site/src/html/planet.html?planet=${planet}`;
});