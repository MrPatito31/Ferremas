document.addEventListener('DOMContentLoaded', () => {
    const derechaDiv = document.getElementById('derecha');

    const loadTemplate = (templateId) => {
        const template = document.getElementById(templateId);
        if (template) {
            derechaDiv.innerHTML = '';
            derechaDiv.appendChild(template.content.cloneNode(true));
        }
    };

    document.getElementById('promociones-btn').addEventListener('click', () => {
        loadTemplate('promociones-template');
    });

    document.getElementById('estrategias-btn').addEventListener('click', () => {
        loadTemplate('estrategias-template');
    });

    document.getElementById('informe-btn').addEventListener('click', () => {
        loadTemplate('informe-template');
    });
});