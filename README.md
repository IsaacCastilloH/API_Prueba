API de Gestión de Biblioteca Digital
Una API RESTful construida con Django y Django REST Framework para gestionar un sistema de biblioteca digital. Esta API proporciona endpoints para gestionar libros, autenticación de usuarios y notificaciones en tiempo real usando WebSockets.

> [!IMPORTANT]
> Este proyecto requiere Python 3.8+ y Docker instalados en tu sistema.

🌟 Características
Operaciones CRUD completas para libros

Autenticación y autorización de usuarios

Notificaciones en tiempo real con WebSockets

Containerización con Docker

Integración con base de datos PostgreSQL

Cobertura de pruebas unitarias

🚀 Instalación
>[!NOTE]
>Asegurarse de tener Docker y Docker Compose instalados en el sistema antes de continuar.

Clonar el repositorio:
bash
git clone https://github.com/IsaacCastilloH/API_Prueba.git

cd API_Prueba



Construir y ejecutar los contenedores Docker:
bash
docker-compose up --build

>[!TIP]
>Si se encuentran problemas de permisos al ejecutar comandos Docker, intentar añadiendo sudo al principio en caso de estar usando linux.

📝 Documentación de la API
Endpoints de Libros
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /api/libros/ | Listar todos los libros |
| POST | /api/libros/ | Crear un nuevo libro |
| GET | /api/libros/{id}/ | Obtener un libro específico |
| PUT | /api/libros/{id}/ | Actualizar un libro específico |
| DELETE | /api/libros/{id}/ | Eliminar un libro específico |

Ejemplo de Objeto Libro
json
{
"titulo": "El Principito",
"autor": "Antoine de Saint-Exupéry",
"fecha_publicacion": "1943-04-06",
"isbn": "978316895384100", 
"paginas": 200
}

🧪 Ejecutar Pruebas
Para ejecutar el conjunto de pruebas:

bash
docker-compose exec web python manage.py test

🛠️ Desarrollo
>[!NOTE]
>El servidor de desarrollo estará disponible en http://localhost:8000

Para acceder a la interfaz de administración de Django:

Crear un superusuario:
bash
docker-compose exec web python manage.py createsuperuser

Visitar http://localhost:8000/admin e iniciar sesión con las credenciales.

📦 Dependencias
Django 4.2+

Django REST Framework

PostgreSQL

Channels (para WebSockets)

Docker

Docker Compose

🔒 Variables de Entorno
>[!IMPORTANT]
>Las variables de entorno se configuran directamente en el archivo docker-compose.yml. No exponer información sensible en repositorios públicos.

🐛 Solución de Problemas
>[!TIP]
>Problemas comunes y sus soluciones:

Problemas de conexión con la base de datos

Verificar que el contenedor de PostgreSQL esté ejecutándose

Comprobar las credenciales en el archivo docker-compose.yml

Verificar la conectividad de red entre contenedores

Permiso denegado

Ejecutar los comandos Docker con sudo

Verificar los permisos de archivos en los volúmenes montados

Puerto ya en uso

Detener cualquier servicio que esté usando el puerto 8000

Cambiar el mapeo de puertos en docker-compose.yml
