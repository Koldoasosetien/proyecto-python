document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("buscadorUsuarios");
    const filas = document.querySelectorAll("#tablaUsuarios tr");

    input.addEventListener("input", () => {
        const filtro = input.value.toLowerCase();

        filas.forEach((fila, index) => {
            if (index < 2) return;

            const celdaNombre = fila.querySelector("td:nth-child(2)");
            if (!celdaNombre) return;

            const nombre = celdaNombre.textContent.toLowerCase();
            fila.style.display = nombre.includes(filtro) ? "" : "none";
        });
    });
});
