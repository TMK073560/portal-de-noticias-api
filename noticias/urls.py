from django.urls import path
from .views import (
    NoticiaCreateView,
    NoticiaDeleteView,
    NoticiaDetailView,
    NoticiaListView,
    NoticiaUpdateView,
    RegistroView,
)

urlpatterns = [
    path("", NoticiaListView.as_view(), name="noticia-list"),
    path("noticia/nueva/", NoticiaCreateView.as_view(), name="noticia-create"),
    path("noticia/<int:pk>/", NoticiaDetailView.as_view(), name="noticia-detail"),
    path(
        "noticia/<int:pk>/editar/",
        NoticiaUpdateView.as_view(),
        name="noticia-update",
    ),
    path(
        "noticia/<int:pk>/borrar/",
        NoticiaDeleteView.as_view(),
        name="noticia-delete",
    ),
    path("registro/", RegistroView.as_view(), name="register"),
]
