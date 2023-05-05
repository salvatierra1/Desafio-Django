from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.veterinaria.forms import ClienteForm
from apps.veterinaria.models import Cliente


# Create your views here.
class ClienteListView(ListView):
    model = Cliente
    template_name ='cliente/lista.html'
    
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name ='cliente/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_clientes')
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name ='cliente/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name ='cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('apps.veterinaria:listado_clientes')

