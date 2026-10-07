from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Noticia
from .permissions import EsStaffOsoloLectura
from .serializers import NoticiaSerializer


class NoticiaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NoticiaSerializer
    permission_classes = [EsStaffOsoloLectura]

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_authenticated and usuario.is_staff:
            return Noticia.objects.all()

        return Noticia.objects.filter(publicada=True)

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class NoticiaRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = NoticiaSerializer
    permission_classes = [EsStaffOsoloLectura]

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_authenticated and usuario.is_staff:
            return Noticia.objects.all()

        return Noticia.objects.filter(publicada=True)


class MisNoticiasAPIView(generics.ListAPIView):
    serializer_class = NoticiaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Noticia.objects.filter(autor=self.request.user)
