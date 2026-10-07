# Pruebas de la API

## Pruebas automáticas

El archivo `noticias/tests_api.py` contiene pruebas para:

- GET público de noticias.
- Bloqueo de POST para usuario común.
- Creación de noticias por usuario staff.
- Validación de `https://` en la imagen.
- Bloqueo de edición de noticias ajenas.
- Endpoint `/api/noticias/mias/`.

Ejecutar:

```powershell
python manage.py test noticias.tests_api
```

## Postman

Importa este archivo en Postman:

`pruebas_api/Portal_Noticias.postman_collection.json`

La colección incluye:

- GET `/api/noticias/`
- GET `/api/noticias/<id>/`
- POST `/api/noticias/`
- PATCH `/api/noticias/<id>/`
- DELETE `/api/noticias/<id>/`
- GET `/api/noticias/mias/`

Para POST, PATCH, DELETE y `/mias/`, configura las variables de la colección:

- `username`: usuario staff/moderador.
- `password`: contraseña de ese usuario.
- `noticia_id`: ID de una noticia creada por ese mismo usuario.

La API acepta autenticación Basic de Django REST Framework para estas pruebas.
