const body = document.querySelector('body'),
        table = document.querySelector('table'),
        sidebar = document.getElementById('sidebar'),
        toggle = body.querySelector(".toggle"),
        searchBtn = body.querySelector(".search-box"),
        modeSwitch = body.querySelector(".toggle-switch"),
        modeText = body.querySelector(".mode-text");

//Botón posición sidebar
toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if (sidebar.classList.contains('close')) {
      localStorage.setItem('sidebarPos', 'close');
    }
    else {
      localStorage.setItem('sidebarPos', 'open');
    }

})

//Botón de búsqueda
searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
})

//Botón modo
modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        modeText.innerText = "Modo Claro";
        localStorage.setItem('mode', 'dark');
        //setItem almacena un par clave, valor.
    } else {
      modeText.innerText = "Modo Oscuro";
      localStorage.setItem('mode', 'light');
    }
  });
  
  var myLink = document.querySelector('a[href="#"]');
  myLink.addEventListener('click', function(e) {
      e.preventDefault();
  });


// function setCookie(cName, cValue, expDays) {
//     const date = new Date();
//     date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000)); //Convierte los días en milisegundos. Tiempo actual + expDays
//     const expires = "expires=" + date.toUTCString(); //Establece la variable "expires" con el formato adecuado
//     document.cookie = cName + "=" + cValue + "; " + expires + "; path=/"; //Establece la cookie con todos los parámetros
// }

// function getCookie(cName) {
//     let name = cName + "=";
//     let ca = document.cookie.split(';');
//     for(let i = 0; i < ca.length; i++) {
//       let c = ca[i];
//       while (c.charAt(0) == ' ') {
//         c = c.substring(1);
//       }
//       if (c.indexOf(name) == 0) {
//         return c.substring(name.length, c.length);
//       }
//     }
//     return "";
//   }


// modeSwitch.addEventListener("click", () => {
//   body.classList.toggle("dark");

//   if (body.classList.contains("dark")) {
//       modeText.innerText = "Modo Claro";
//       setCookie('mode', 'dark', 10);
//   } else {
//       modeText.innerText = "Modo Oscuro";
//       setCookie('mode', 'light', 10);
//   }
// });
