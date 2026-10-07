from django.conf import settings
from django.db import models
from django.urls import reverse


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    url_imagen = models.URLField(max_length=500)
    descripcion = models.TextField(blank=True)
    publicada = models.BooleanField(default=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="noticias",
    )
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creada"]
        verbose_name = "noticia"
        verbose_name_plural = "noticias"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("noticia-detail", kwargs={"pk": self.pk})
