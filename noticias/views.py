from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from .forms import NoticiaForm
from .models import Noticia


class NoticiaListView(ListView):
    model = Noticia
    context_object_name = "noticias"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(publicada=True)


class NoticiaDetailView(DetailView):
    model = Noticia
    context_object_name = "noticia"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(publicada=True)


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class NoticiaCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class NoticiaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm

    def test_func(self):
        noticia = self.get_object()
        return self.request.user.is_staff and noticia.autor == self.request.user


class NoticiaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Noticia
    success_url = reverse_lazy("noticia-list")

    def test_func(self):
        noticia = self.get_object()
        return self.request.user.is_staff and noticia.autor == self.request.user


class RegistroView(FormView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("noticia-list")

    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return super().form_valid(form)
