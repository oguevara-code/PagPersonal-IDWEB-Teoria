document.addEventListener("DOMContentLoaded", () => {
    cargarComentarios();
});

// Pide los comentarios al backend
function cargarComentarios() {
    fetch("/comentarios")
        .then(response => response.json())
        .then(data => mostrarComentarios(data))
        .catch(error => {
            const contenedor = document.getElementById("lista-comentarios");
            contenedor.innerHTML = "<p>Error al cargar los comentarios.</p>";
        });
}

// Muestra los comentarios en la página
function mostrarComentarios(comentarios) {
    const contenedor = document.getElementById("lista-comentarios");
    contenedor.innerHTML = "";

    if (comentarios.length === 0) {
        contenedor.innerHTML = "<p>No hay comentarios aún.</p>";
        return;
    }

    comentarios.forEach(comentario => {
        const div = document.createElement("div");
        div.classList.add("comentario");

        div.innerHTML = `
            <h4>${comentario.nombre}</h4>
            <p>${comentario.mensaje}</p>
            <small>${comentario.fecha}</small>
        `;

        contenedor.appendChild(div);
    });
}