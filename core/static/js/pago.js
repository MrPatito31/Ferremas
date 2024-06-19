document.addEventListener('DOMContentLoaded', () => {
    const derechaDiv = document.getElementById('despachos');

    const loadTemplate = (templateId) => {
        const template = document.getElementById(templateId);
        if (template) {
            derechaDiv.innerHTML = '';
            derechaDiv.appendChild(template.content.cloneNode(true));
        }
    };

    document.getElementById('tienda-btn').addEventListener('click', () => {
        loadTemplate('tienda-template');
    });

    document.getElementById('domicilio-btn').addEventListener('click', () => {
        loadTemplate('domicilio-template');
    });
});