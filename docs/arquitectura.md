# Arquitectura del Proyecto

## Estructura General
El proyecto sigue la arquitectura estándar de Django, con una aplicación principal llamada `library_app`.

### Componentes Clave
- **library/settings.py:** Configuración global del proyecto.
- **library_app/models.py:** Modelos de datos para libros, préstamos y reservas.
- **library_app/serializers.py:** Serializadores para convertir datos entre JSON y modelos.
- **library_app/views.py:** Lógica de negocio y controladores de la API.
- **library_app/consumers.py:** Manejo de WebSockets para notificaciones en tiempo real.

### Integración con Docker
El proyecto utiliza Docker para simplificar la configuración del entorno. Los servicios principales son:
- **web:** Contenedor que ejecuta la aplicación Django.
- **db:** Contenedor que ejecuta PostgreSQL como base de datos.