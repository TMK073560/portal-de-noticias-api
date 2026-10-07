PORTAL DE NOTICIAS - DJANGO 5

Este proyecto usa SOLO Django y SQLite.

Después de descomprimir:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

PERMISOS:
- Visitante: puede ver noticias publicadas.
- Usuario registrado normal: puede iniciar sesión y ver noticias.
- Usuario staff: puede publicar noticias.
- Editar y borrar: solo si además de ser staff, es autor de la noticia.

El autor se asigna automáticamente con request.user.
No se incluye autor ni creada en el formulario.
La URL de la imagen debe comenzar con https://.


============================================================
API REST CON DJANGO REST FRAMEWORK
============================================================

Este proyecto SI incluye Django REST Framework.

Asegúrate de tenerlo instalado:
    pip install djangorestframework

Rutas de la API:

GET /api/noticias/
    Lista las noticias publicadas.
    Los usuarios staff pueden ver también las no publicadas.

POST /api/noticias/
    Crea una noticia.
    Solo usuarios autenticados con is_staff=True.
    El autor se asigna automáticamente con request.user.

GET /api/noticias/<id>/
    Devuelve el detalle de una noticia.

PUT /api/noticias/<id>/
PATCH /api/noticias/<id>/
DELETE /api/noticias/<id>/
    Solo el usuario staff que además sea autor de la noticia.

GET /api/noticias/mias/
    Requiere autenticación.
    Devuelve las noticias cuyo autor es request.user.

ROLES:
- Guest: solo lectura de noticias públicas.
- Usuario común: lectura de noticias públicas.
- Staff/Moderador: puede publicar y modificar sus propias noticias.
- Superusuario/Admin: administración general desde /admin/.

SEGURIDAD API:
- Serializer con lista explícita de campos.
- autor e id/creada son de solo lectura.
- El autor nunca se recibe desde el cliente.
- Validación de url_imagen para exigir https://.
- Permiso personalizado de solo lectura para público.
- Throttling básico para usuarios anónimos y autenticados.

IMPORTANTE:
Esta versión usa la autenticación de sesión de Django/DRF.
No incluye JWT porque JWT requiere otro paquete adicional como
djangorestframework-simplejwt. Si la evaluación exige JWT, debe agregarse
ese paquete además de djangorestframework.


============================================================
PRUEBAS DE API
============================================================

- noticias/tests_api.py
  Pruebas automáticas con APITestCase de Django REST Framework.

- pruebas_api/Portal_Noticias.postman_collection.json
  Colección lista para importar en Postman.

- pruebas_api/pruebas_api.http
  Ejemplos manuales de peticiones HTTP.

Ejecutar pruebas automáticas:
    python manage.py test noticias.tests_api
