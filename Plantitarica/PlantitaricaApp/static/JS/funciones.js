
    var elementosNavbar = document.querySelectorAll('.mini-nav ul li');
    elementosNavbar.forEach(function(elemento) {
        elemento.addEventListener('click', function() {
            elementosNavbar.forEach(function(el) {
                el.classList.remove('active');
            });
            elemento.classList.add('active');
        });
    });
    


function setAction(form) {
    var currentPage = window.location.href;
    form.querySelector("#pagina_destino").value = currentPage;
}

function alternarCarro() {
    var elementos = document.getElementsByClassName('carro_oculto');
    for (var i = 0; i < elementos.length; i++) {
        if (elementos[i].style.display === 'none' || elementos[i].style.display === '') {
            elementos[i].style.display = 'block'; 
        } else {
            elementos[i].style.display = 'none';
        }
    }
}

function mostrarCarro() {
    var elementos = document.getElementsByClassName('carro_oculto');
    for (var i = 0; i < elementos.length; i++) {
        elementos[i].style.display = 'block'; 
    }
}
function ocultarCarro() {
    var elementos = document.getElementsByClassName('carro_oculto');
    for (var i = 0; i < elementos.length; i++) {
        elementos[i].style.display = 'none';
    }
}

function alternarMenu() {
    var elemento = document.getElementById('menu');
    if (elemento.style.display === 'none' || elemento.style.display === '') {
        elemento.style.display = 'block'; 
    } else {
        elemento.style.display = 'none';
    }
}