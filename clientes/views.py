from django.shortcuts import render
from django.views.generic import ListView,CreateView
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
