Asegúrate de tener instalado lo siguiente en tu máquina:

Docker: Instalación de Docker
Docker Compose: Instalación de Docker Compose
Configuración y Ejecución
Clona este repositorio:

bash
Copy code
git clone https://github.com/migueload/django-rest-api-contactos.git
Navega al directorio del proyecto:

bash
Copy code
cd django-rest-api-contactos
Construye y ejecuta el contenedor de Docker:

bash
Copy code
docker-compose up --build
Este comando construirá la imagen de Docker y ejecutará el contenedor, haciendo que la API esté disponible en http://127.0.0.1:8000/.

Abre tu navegador y visita la URL de administración de Django para verificar que la API esté funcionando correctamente:

http://127.0.0.1:8000/admin/
Puedes usar las credenciales predeterminadas (nombre de usuario: admin, contraseña: admin) para iniciar sesión.

Uso de Postman
Puedes usar Postman para realizar solicitudes a la API y probar las operaciones CRUD. Aquí hay algunos ejemplos:

Crear un contacto:

Método: POST
URL: http://127.0.0.1:8000/api/contacts/
Headers:
Content-Type: application/json
Authorization: Token <tu-token>
Cuerpo (raw JSON):
json
Copy code
{
  "name": "Nombre del Contacto",
  "phone": "123-456-7890",
  "email": "correo@ejemplo.com"
}
Leer un contacto:

Método: GET
URL: http://127.0.0.1:8000/api/contacts/<id>/
Headers:
Authorization: Token <tu-token>
Actualizar un contacto:

Método: PUT
URL: http://127.0.0.1:8000/api/contacts/<id>/
Headers:
Content-Type: application/json
Authorization: Token <tu-token>
Cuerpo (raw JSON):
json
Copy code
{
  "name": "Nuevo Nombre",
  "phone": "Nuevo Teléfono",
  "email": "nuevo.correo@ejemplo.com"
}
Eliminar un contacto:

Método: DELETE
URL: http://127.0.0.1:8000/api/contacts/<id>/
Headers:
Authorization: Token <tu-token>
Asegúrate de reemplazar <tu-token> con el token de autenticación adecuado y <id> con el ID del contacto correspondiente.

Detener y Limpiar
Para detener el contenedor, puedes presionar Ctrl + C en la terminal donde se está ejecutando el contenedor. Para limpiar los recursos de Docker, ejecuta:

bash
Copy code
docker-compose down
Esto detendrá y eliminará el contenedor, así como cualquier red o volumen creado durante la ejecución.
