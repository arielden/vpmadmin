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

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
})

searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");
    table.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        modeText.innerText = "Light mode";
        setCookie('mode', 'dark', 10);
    } else {
        modeText.innerText = "Dark mode";
        setCookie('mode', 'light', 10);

    }
});

var myLink = document.querySelector('a[href="#"]');
myLink.addEventListener('click', function(e) {
    e.preventDefault();
});