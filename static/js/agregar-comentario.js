document.getElementById("form-comentario")
    .addEventListener("submit", enviarComentario);

// Función para enviar el comentario
function enviarComentario(event) {
    event.preventDefault(); // evita recargar la página

    const nombre = document.getElementById("nombre").value.trim();
    const mensaje = document.getElementById("mensaje").value.trim();
    const estado = document.getElementById("mensaje-estado");

    // Validación simple
    if (nombre === "" || mensaje === "") {
        estado.textContent = "Por favor completa todos los campos.";
        return;
    }

    // Enviar datos al backend
    fetch("/comentarios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nombre: nombre,
            mensaje: mensaje
        })
    })
    .then(response => response.json())
    .then(data => {
        estado.textContent = "Comentario enviado correctamente";
        document.getElementById("form-comentario").reset();

        // Redirige después de 1 segundo
        setTimeout(() => {
            window.location.href = "/comentarios";
        }, 1000);
    })
    .catch(error => {
        estado.textContent = "Error al enviar el comentario.";
    });
}