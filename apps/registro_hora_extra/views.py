from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada) # olhando somente empresa logada e do funcionario
        return queryset

# UPDATE possui o objeto object dentro dele..
class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']