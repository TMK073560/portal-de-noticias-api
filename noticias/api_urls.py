from django.urls import path

from .api_views import (
    MisNoticiasAPIView,
    NoticiaListCreateAPIView,
    NoticiaRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("noticias/", NoticiaListCreateAPIView.as_view(), name="api-noticia-list"),
    path(
        "noticias/<int:pk>/",
        NoticiaRetrieveUpdateDestroyAPIView.as_view(),
        name="api-noticia-detail",
    ),
    path(
        "noticias/mias/",
        MisNoticiasAPIView.as_view(),
        name="api-mis-noticias",
    ),
]
