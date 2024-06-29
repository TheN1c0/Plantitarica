    //agregar la clase 'active' al elemento clickeado y quitarla de los demás
    var elementosNavbar = document.querySelectorAll('.mini-nav ul li');
    elementosNavbar.forEach(function(elemento) {
        elemento.addEventListener('click', function() {
            elementosNavbar.forEach(function(el) {
                el.classList.remove('active');
            });
            elemento.classList.add('active');
        });
    });
    
s

function setAction(form) {
    var currentPage = window.location.href;
    form.querySelector("#pagina_destino").value = currentPage;
}

function alternarCarro() {
    var elementos = document.getElementsByClassName('carro_oculto');
    for (var i = 0; i < elementos.length; i++) {
        if (elementos[i].style.display === 'none' || elementos[i].style.display === '') {
            elementos[i].style.display = 'block'; // Asegúrate de que este display se ajuste a tu layout
        } else {
            elementos[i].style.display = 'none';
        }
    }
}

function mostrarCarro() {
    var elementos = document.getElementsByClassName('carro_oculto');
    for (var i = 0; i < elementos.length; i++) {
        elementos[i].style.display = 'block'; // Cambia 'block' a 'flex' o 'grid' según tu layout
    }
}
function ocultarCarro() {
    var elementos = document.getElementsByClassName('carro_oculto');
    for (var i = 0; i < elementos.length; i++) {
        elementos[i].style.display = 'none';
    }
}