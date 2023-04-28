from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .models import Obras, Contatos,Check_List
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    msg = {'mensagem':'ola mundo'}   
    return render(request, 'cadastros/index.html', msg)


class ObrasCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Obras
    fields = ['status','DC', 'Colaborador_1', 'Colaborador_2','Fotos', 'status_final', 'Check1']
    template_name = 'cadastros/form_upload.html'
    success_url = reverse_lazy('cadastrar-Obra')
   
#####################LISTAS###################

class ObrasList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Obras
    template_name = 'cadastros/listas/obra.html'

class ObrasContato(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Contatos
    template_name = 'cadastros/listas/contatos.html'

##################### ATUALIZAR LISTA (EDITE)###################


class ObrasUpdate(UpdateView):
    model = Obras
    fields = ['DC', 'Colaborador_1', 'Colaborador_2','Fotos','status_final']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-Obra')

################### Chek list Segurança #################################

class Check_listCreat(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Check_List
    fields = '__all__'
    template_name = 'cadastros/Form_checklist.html'
    success_url = reverse_lazy('cadastrar-Checklist')

class Check_list(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Check_List
    template_name = 'cadastros/listas/checklist.html'


###################EXporta -csv #################################