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
document.addEventListener("DOMContentLoaded", async function () {
    try {
        const response = await fetch("http://127.0.0.1:5000/cursores"); // Llamada a la API
        const datos = await response.json(); // Convierte la respuesta en JSON

        const contenedor = document.querySelector(".padre"); // Div donde se insertan las cards

        datos.forEach((cursor) => {
            // Crea la estructura de la card
            const card = document.createElement("div");
            card.classList.add("card");

            card.innerHTML = `
                <h2>${cursor.Nombres}</h2>
                <div class="cursor-preview">
                    <img src="${cursor['img 1']}" alt="Arrow Cursor">
                    <img src="${cursor['img 2']}" alt="Hand Cursor">
                    <img src="${cursor['img 3']}" alt="Help Cursor">
                </div>
                <div class="buttons">
                    <a href="#" download class="btn">
                        <i class="bi bi-download"></i>
                    </a>
                    <a href="${cursor.Fuente}" target="_blank" class="btn">
                        <i class="bi bi-box-arrow-up-right"></i>
                    </a>
                    <a href="#" download class="btn">
                        <i class="bi bi-mouse"></i>
                    </a>
                </div>
            `;

            contenedor.appendChild(card); // Agrega la card al div .padre
        });

    } catch (error) {
        console.error("Error al cargar los cursores:", error);
    }
});
