# 🐾 Sistema de Gestión de Historial Clínico Veterinario

Este proyecto es una aplicación web desarrollada en Django que permite gestionar de manera eficiente el historial clínico de mascotas en una clínica veterinaria. Incluye funciones para registrar propietarios, animales, agendar consultas médicas, y mantener un historial médico por mascota.

## 🚀 Características Principales

- Registro y administración de propietarios de mascotas
- Registro de animales con detalles como especie, raza y fecha de nacimiento
- Gestión de consultas médicas por mascota
- Historial médico detallado por cada paciente
- Sistema de autenticación de usuarios
- Panel de administración personalizado con Django Admin
- Interfaz amigable usando HTML, CSS y JavaScript

## 🛠️ Tecnologías Utilizadas

- Python 3.10+
- Django 4.x
- SQLite3 (por defecto, pero fácilmente adaptable a PostgreSQL/MySQL)
- HTML5 / CSS3 / JavaScript
- Bootstrap (opcional)
- Django Admin

## 📦 Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/tu-usuario/historial-clinico-veterinario.git
cd historial-clinico-veterinario





historial_clinico_veterinario/
├── gestion_clinicaApp/         # App principal con modelos y vistas
├── usuarios/                   # App para autenticación y usuarios
├── templates/                  # Plantillas HTML
├── static/                     # Archivos CSS/JS/Imágenes
├── historial_clinico_veterinario/  # Configuración principal del proyecto
├── db.sqlite3
├── manage.py
└── README.md


📚 Modelos Clave
Propietario: Nombre, contacto, dirección

Animal: Nombre, especie, raza, fecha de nacimiento, propietario

ConsultaMedica: Fecha, motivo, diagnóstico, tratamiento, animal

Usuario (custom): Sistema personalizado de usuarios (opcional)

🗓️ Próximas Funcionalidades
Sistema de notificaciones por correo

Reportes en PDF de historiales médicos

Carga de archivos/imágenes clínicas

Buscador y filtros por especie o dueño

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Puedes crear un fork del proyecto y enviar un pull request con tus mejoras o sugerencias.


📧 Contacto
Desarrollado por José Luis Duarte
Correo: joseluisduartepachon@gmail.com
Teléfono: 3126305190
