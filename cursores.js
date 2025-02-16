async function cargarCursores() {
    try {
        const response = await fetch("http://127.0.0.1:5000/cursores"); // Llamada a la API
        const datos = await response.json(); // Convierte la respuesta en JSON
        console.log("Datos de la api", datos)
        const contenedor = document.querySelector(".padre"); // Div donde se insertan las cards
        if (!contenedor) return;

        contenedor.innerHTML = ""; // Limpia antes de insertar nuevas tarjetas

        datos.forEach((cursor) => {
            const card = document.createElement("div");
            card.classList.add("card");
            console.log(`Procesando cursor ${index + 1}:`, cursor); // Depuración de cada objeto recibido

            // Verifica que las imágenes existen en la respuesta
            const img1 = cursor["img 1"];
            const img2 = cursor["img 2"];
            const img3 = cursor["img 3"];

            console.log(`Imágenes del cursor ${index + 1}:`, img1, img2, img3);
            card.innerHTML = `
                <h2>${cursor.Nombres}</h2>
                <div class="cursor-preview">
                    <img src="${img1}" alt="Arrow Cursor">
                    <img src="${img2}" alt="Hand Cursor">
                    <img src="${img3}" alt="Help Cursor">
                </div>
                <div class="buttons">
                    <a href="#" download class="btn">
                        <i class="bi bi-download"></i>
                    </a>
                    <a href="${cursor.Fuente}" class="btn external-link" data-url="${cursor.Fuente}">
                        <i class="bi bi-box-arrow-up-right"></i>
                    </a>
                    <a href="#" download class="btn">
                        <i class="bi bi-mouse"></i>
                    </a>
                </div>
            `;

            contenedor.appendChild(card);
        });

    } catch (error) {
        console.error("Error al cargar los cursores:", error);
    }
}

// Evento global para manejar enlaces externos y enviarlos a Flask
document.body.addEventListener("click", function (event) {
    const target = event.target.closest("a.external-link"); // Solo enlaces con la clase "external-link"
    if (target) {
        event.preventDefault(); // Evita la navegación en Electron

        const url = target.getAttribute("data-url"); // Obtiene la URL del enlace

        fetch("http://127.0.0.1:5000/abrir-url", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url }) // Envía la URL a Flask
        })
        .then(response => response.json())
        .then(data => console.log(data.message))
        .catch(error => console.error("Error enviando la URL:", error));
    }
});
