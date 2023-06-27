const header = new URL(document.location).searchParams,
  sign_name = document.getElementById("sign_name"),
  sign_date = document.getElementById("sign_date"),
  sign_img = document.getElementById("sign_img"),
  constellation = document.getElementById("constellation_img"),
  info = document.getElementById("sign_info"),
  famous = document.getElementById("famous"),
  women = document.getElementById("famous_women"),
  men = document.getElementById("famous_men");

fetch('/static/json/signs.json')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    data.forEach(line => {
        if (line.sign == header.get("sign")) {
            sign_name.innerHTML = `${line.sign}`;
            sign_date.innerHTML = `${line.date}`;
            sign_img.src = `${line.img}`;
            constellation.src = `${line.constellation}`;
            info.innerHTML = `${line.characteristic}`;
            famous.innerHTML += `${line.famous}`;
            women.innerHTML = `${line.women}`;
            men.innerHTML = `${line.men}`;
        }
    })
  });