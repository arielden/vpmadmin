const body = document.querySelector('body'),
        table = document.querySelector('table'),
        sidebar = body.querySelector('nav'),
        toggle = body.querySelector(".toggle"),
        searchBtn = body.querySelector(".search-box"),
        modeSwitch = body.querySelector(".toggle-switch"),
        modeText = body.querySelector(".mode-text");

function setCookie(cName, cValue, expDays) {
    const date = new Date();
    date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000)); //Convierte los días en milisegundos. Tiempo actual + expDays
    const expires = "expires=" + date.toUTCString(); //Establece la variable "expires" con el formato adecuado
    document.cookie = cName + "=" + cValue + "; " + expires + "; path=/"; //Establece la cookie con todos los parámetros
}

function getCookie(cName) {
    let name = cName + "=";
    let ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    // if (sidebar.classList.contains("close")) {
    //     document.cookie = "position=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    // } else {
    //     setCookie('position', 'close', 10);
    // }
})

searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");
    // table.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        modeText.innerText = "Modo Claro";
        setCookie('mode', 'dark', 10);
    } else {
        modeText.innerText = "Modo Oscuro";
        setCookie('mode', 'light', 10);
    }
});

var myLink = document.querySelector('a[href="#"]');
myLink.addEventListener('click', function(e) {
    e.preventDefault();
});