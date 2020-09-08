from django.urls import path
from .views import (FuncionariosList,
                    FuncionarioEdit,
                    FuncionarioDelete,
                    FuncionarioNovo,
                    relatorio_funcionarios,
                    Pdf,
                    PdfDebug
                    )

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('novo', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('pdf-reportlab', relatorio_funcionarios, name='pdf_reportlab'),
    path('pdf-html', Pdf.as_view(), name='pdf_html'),
    path('pdf-html-debug', PdfDebug.as_view(), name='pdf_html_debug'),
]
