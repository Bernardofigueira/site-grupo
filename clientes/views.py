from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy #O reverse_lazy redireciona para uma pagina
from .models import Cliente
from .forms import ClienteForm #Importa a classe do arquivo form.py
# Create your views here.
class Home(ListView):
    def get(self,request):
        return render(request, 'clientes/homepage.html')


def esporte(request):
    return render(request, 'clientes/esporte.html')

def cultura(request):
    return render(request, 'clientes/cultura.html')

def economia(request):
    return render(request, 'clientes/economia.html')

def login(request):
    return render(request, 'clientes/login.html')

class Cadastro(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cadastro.html'   #Gera o template do formulario
    success_url = reverse_lazy('inicio')
