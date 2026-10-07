from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Noticia


User = get_user_model()


class NoticiaAPITests(APITestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username="moderador",
            password="ClaveSegura123!",
            is_staff=True,
        )

        self.usuario = User.objects.create_user(
            username="usuario",
            password="ClaveSegura123!",
        )

        self.noticia = Noticia.objects.create(
            titulo="Noticia de prueba",
            url_imagen="https://example.com/imagen.jpg",
            descripcion="Contenido de prueba",
            publicada=True,
            autor=self.staff,
        )

    def test_guest_puede_listar_noticias(self):
        respuesta = self.client.get("/api/noticias/")
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)

    def test_usuario_comun_no_puede_publicar(self):
        self.client.force_authenticate(user=self.usuario)

        datos = {
            "titulo": "Noticia usuario común",
            "url_imagen": "https://example.com/usuario.jpg",
            "descripcion": "No debería poder publicarse.",
            "publicada": True,
        }

        respuesta = self.client.post("/api/noticias/", datos, format="json")
        self.assertEqual(respuesta.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_puede_publicar(self):
        self.client.force_authenticate(user=self.staff)

        datos = {
            "titulo": "Nueva noticia del moderador",
            "url_imagen": "https://example.com/nueva.jpg",
            "descripcion": "Noticia creada mediante la API.",
            "publicada": True,
        }

        respuesta = self.client.post("/api/noticias/", datos, format="json")

        self.assertEqual(respuesta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(respuesta.data["autor"], self.staff.username)

    def test_url_imagen_debe_ser_https(self):
        self.client.force_authenticate(user=self.staff)

        datos = {
            "titulo": "URL no segura",
            "url_imagen": "http://example.com/insegura.jpg",
            "descripcion": "Debe ser rechazada.",
            "publicada": True,
        }

        respuesta = self.client.post("/api/noticias/", datos, format="json")
        self.assertEqual(respuesta.status_code, status.HTTP_400_BAD_REQUEST)

    def test_staff_no_puede_editar_noticia_ajena(self):
        otro_staff = User.objects.create_user(
            username="otro_moderador",
            password="ClaveSegura123!",
            is_staff=True,
        )

        noticia_ajena = Noticia.objects.create(
            titulo="Noticia ajena",
            url_imagen="https://example.com/ajena.jpg",
            descripcion="Pertenece a otro moderador.",
            publicada=True,
            autor=otro_staff,
        )

        self.client.force_authenticate(user=self.staff)

        respuesta = self.client.patch(
            f"/api/noticias/{noticia_ajena.pk}/",
            {"titulo": "Intento de cambio"},
            format="json",
        )

        self.assertEqual(respuesta.status_code, status.HTTP_403_FORBIDDEN)

    def test_endpoint_mias_devuelve_solo_noticias_del_usuario(self):
        self.client.force_authenticate(user=self.staff)

        respuesta = self.client.get("/api/noticias/mias/")

        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respuesta.data), 1)
        self.assertEqual(respuesta.data[0]["titulo"], self.noticia.titulo)
