// frontend/static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    const loadButton = document.getElementById('add-employee-btn'); // Usamos el botón de nuevo empleado para la prueba
    const tableBody = document.querySelector('#employees-table tbody');

    loadButton.addEventListener('click', async () => {
        tableBody.innerHTML = '<tr><td colspan="5">Llamando a la API...</td></tr>';
        try {
            // Llamamos a la raíz de la API
            const response = await fetch('/api/');
            const text = await response.text();
            
            if (!response.ok) {
                throw new Error(`Error ${response.status}: ${text}`);
            }

            // Mostramos el "HOLA MUNDO" en la tabla
            tableBody.innerHTML = `<tr><td colspan="5">Respuesta del servidor: ${text}</td></tr>`;

        } catch (error) {
            console.error("Falló la llamada a la API:", error);
            tableBody.innerHTML = `<tr><td colspan="5">Falló la llamada: ${error.message}</td></tr>`;
        }
    });
});