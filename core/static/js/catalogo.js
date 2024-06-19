/*ABRIR CARRO*/
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("opencarro").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "block"; // Mostrar overlay
        document.getElementById("carro").style.display = "block"; // Mostrar ventana
    });
    document.getElementById("closecarro").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "none"; // Ocultar overlay
        document.getElementById("carro").style.display = "none";// Ocultar ventana
    });

/*ABRIR HISTORIAL*/
    document.getElementById("openhistorial").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "block"; // Mostrar overlay
        document.getElementById("historial").style.display = "block";// Mostrar ventana
    });
    document.getElementById("closehistorial").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "none"; // Ocultar overlay
        document.getElementById("historial").style.display = "none";// Ocultar ventana
    });

/*ABRIR PERFIL*/
    document.getElementById("openperfil").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "block"; // Mostrar overlay
        document.getElementById("perfil").style.display = "block";// Mostrar ventana
    });

    document.getElementById("closeperfil").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "none"; // Ocultar overlay
        document.getElementById("perfil").style.display = "none"; // Ocultar ventana
    });
});