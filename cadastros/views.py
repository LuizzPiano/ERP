from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Obras
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from usuarios.models import Perfil
from django.contrib.auth.models import User



class ObrasCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Obras
    fields = ['DC', 'Colaborador_1', 'Colaborador_2']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastrar-Obra')

    def get_queryset(self):
        self.object_list = Perfil.objects.filter(usuario=self.request.user)
        return self.object_list

 
    
#####################LISTAS###################


class ObrasList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Obras
    template_name = 'cadastros/listas/obra.html'

    def get_queryset(self):
        self.object_list = Perfil.objects.filter(usuario=self.request.user)
        return self.object_list
    

    




   
#####################ATUALIZAR LISTA###################


class ObrasUpdate(UpdateView):
    model = Obras
    fields = ['DC', 'Colaborador_1', 'Colaborador_2','Fotos']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-Obra')

   