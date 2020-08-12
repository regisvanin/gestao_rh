from django.db import models
from apps.funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT) # seta nulo quando for deletado o funcionario / null and black

    def __str__(self):
        return self.descricao