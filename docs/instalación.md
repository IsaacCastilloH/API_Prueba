# Guía de Instalación

## Requisitos Previos
- Docker y Docker Compose instalados.
- Python 3.8+.

## Pasos de Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/IsaacCastilloH/API_Prueba.git

cd API_Prueba

Construir y ejecutar los contenedores:
docker-compose up --build

Ejecutar las migraciones:
docker-compose exec web python manage.py migrate

Crear un superusuario (opcional):

docker-compose exec web python manage.py createsuperuser

Acceder al servidor en http://localhost:8000/admin.