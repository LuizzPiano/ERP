from django import forms
from django.db import models
 
class Colaboradores(models.Model):
    nome = models.CharField(max_length=50)
    ind = models.CharField(max_length=50)
    data_admissao = models.DateField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        unique_together = ['nome', 'data_admissao']

    class Meta:
        verbose_name ="Colaboradores"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return str(self.nome) 


class Base(models.Model):
    nome = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=30)
    disponivel = models.BooleanField(default=True)

    class Meta:
        unique_together = ['nome', 'rua', 'numero']

    def __str__(self):
        return self.nome


class Folga(models.Model):
    data_folga = models.DateField()
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ['data_folga','colaborador']

    def __str__(self):
        return str(self.data) +' - '+ str(self.colaborador)


class Escala(models.Model):
    data = models.DateField(null=True,)
    base = models.ForeignKey(Base, on_delete=models.SET_NULL, null=True)
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.SET_NULL, null=True)
    disponivel = models.BooleanField(default=True)

    class Meta:
        unique_together = [ 'colaborador', 'data']

    def __str__(self):
        return str(self.colaborador)
