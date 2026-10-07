from rest_framework.permissions import SAFE_METHODS, BasePermission


class EsStaffOsoloLectura(BasePermission):
    """
    Cualquier visitante puede leer.
    Solo usuarios autenticados y staff pueden crear.
    Para editar o borrar, además deben ser autores de la noticia.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
            and request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
            and request.user.is_staff
            and obj.autor == request.user
        )
