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