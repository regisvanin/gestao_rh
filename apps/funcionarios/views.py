from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.base import View, TemplateView

from .models import Funcionario

# IMPORT PARA O XHTML2PDF
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

# IMPORT PARA  O REPORTLAV
import io
from reportlab.pdfgen import canvas

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)  # cria o objeto em memoria e nao manda para o banco
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username = username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)


def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #adicionado para baixar o arquivo e nao abrir na pagina
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(200, 810, "Relatório de Funcionarios")   # escrevendo em X e Y
    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)
    str_ = 'Nome: %s | Hora Extra: %f'
    y = 790
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas_extra))
        y -= 20
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):
    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')

class PdfDebug(TemplateView):
    template_name = 'funcionarios/relatorio.html'
