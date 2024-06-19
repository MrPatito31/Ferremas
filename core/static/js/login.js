document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("register-link").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "block"; // Mostrar overlay
        document.getElementById("register").style.display = "block"; // Mostrar ventana
    });
    document.getElementById("closeregister").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "none"; // Ocultar overlay
        document.getElementById("register").style.display = "none";// Ocultar ventana
    });
});