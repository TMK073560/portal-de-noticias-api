from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude = ("autor", "creada")
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Título de la noticia"}),
            "url_imagen": forms.URLInput(
                attrs={"placeholder": "https://ejemplo.com/noticia.jpg"}
            ),
            "descripcion": forms.Textarea(
                attrs={"rows": 8, "placeholder": "Contenido de la noticia"}
            ),
        }

    def clean_url_imagen(self):
        url = self.cleaned_data["url_imagen"].strip()
        if not url.startswith("https://"):
            raise forms.ValidationError(
                "La URL de la imagen debe comenzar con https://"
            )
        return url
