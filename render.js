document.addEventListener("DOMContentLoaded", () => {
    const contenido = document.querySelector(".contenido"); // Asegúrate de seleccionar correctamente

    function cargarVista(page) {
        fetch(`views/${page}`)
            .then(response => response.text())
            .then(html => {
                contenido.innerHTML = html; // Inyectar HTML en el div
            })
            .catch(error => console.error("Error cargando la vista:", error));
    }

    // Cargar la vista inicial "cursores.html"
    cargarVista("cursores.html");

    document.querySelectorAll(".menu a").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const page = this.getAttribute("data-page");
            cargarVista(page);
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const menuLinks = document.querySelectorAll('.menu a');
    const contenido = document.querySelector('.contenido');

    // Activar el enlace "Cursores" por defecto
    const defaultLink = document.querySelector('.menu a[data-page="cursores.html"]');
    if (defaultLink) {
        defaultLink.classList.add('active');
        // Cargar el contenido de "cursores.html" por defecto
        const page = defaultLink.getAttribute('data-page');
        if (page) {
            fetch(page)
                .then(response => response.text())
                .then(data => {
                    contenido.innerHTML = data;
                })
                .catch(err => console.error('Error loading page:', err));
        }
    }

    // Manejar el clic en los enlaces del menú
    menuLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            // Remover la clase 'active' de todos los enlaces
            menuLinks.forEach(l => l.classList.remove('active'));
            // Agregar la clase 'active' al enlace clickeado
            this.classList.add('active');
            // Cambiar el contenido dinámico
            const page = this.getAttribute('data-page');
            if (page) {
                fetch(page)
                    .then(response => response.text())
                    .then(data => {
                        contenido.innerHTML = data;
                    })
                    .catch(err => console.error('Error loading page:', err));
            }
        });
    });
});