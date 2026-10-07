from rest_framework import serializers

from .models import Noticia


class NoticiaSerializer(serializers.ModelSerializer):
    autor = serializers.CharField(source="autor.username", read_only=True)

    class Meta:
        model = Noticia
        fields = [
            "id",
            "titulo",
            "url_imagen",
            "descripcion",
            "publicada",
            "autor",
            "creada",
        ]
        read_only_fields = ["id", "autor", "creada"]

    def validate_url_imagen(self, value):
        if not value.startswith("https://"):
            raise serializers.ValidationError(
                "La URL de la imagen debe comenzar con https://"
            )
        return value
