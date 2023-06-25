const header = new URL(document.location).searchParams,
      sign = document.getElementById("sign_horoscope"),
      month = document.getElementById("month_horoscope");

switch (header.get("sign")) {
    case "Козерог":
        sign.innerHTML += "козерогов на";
        break;
    case "Водолей":
        sign.innerHTML += "водолеев на";
        break;
    case "Рыбы":
        sign.innerHTML += "рыб на";
        break;
    case "Овен":
        sign.innerHTML += "овнов на";
        break;
    case "Телец":
        sign.innerHTML += "тельцов на";
        break;
    case "Близнецы":
        sign.innerHTML += "близнецов на";
        break;
    case "Рак":
        sign.innerHTML += "раков на";
        break;
    case "Лев":
        sign.innerHTML += "львов на";
        break;
    case "Дева":
        sign.innerHTML += "дев на";
        break;
    case "Весы":
        sign.innerHTML += "весов на";
        break;
    case "Скорпион":
        sign.innerHTML += "скорпионов на";
        break;
    case "Стрелец":
        sign.innerHTML += "стрельцов на";
        break;
}

const date = new Date();
const monthName = date.toLocaleString('default', { month: 'long' });
month.innerHTML = `${monthName}`;