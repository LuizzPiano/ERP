
from datetime import timedelta, timezone
import datetime
from django.db import models
from django.contrib.auth.models import User


def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


def upload_img_obra(instance, filename):
    return f"{instance.DC}-{filename}"




class Obras(models.Model):
    Status_choices = (
        ("Não iniciado", "Não iniciado"),
        ("Iniciado", "Iniciado"),
        ("Pendênciado", "Pendênciado")
    )
    Status_final_choices = (
        ("Não iniciado", "Não iniciado"),
        ("Pendênciado", "Pendênciado"),
        ("Em andamento", "Em andamento"),
        ("Finalizado", "Finalizado")
    )

    

    status = models.CharField(max_length=12, choices=Status_choices, blank=False, null=False)
    DC = models.CharField(max_length=50)
    Colaborador_1 = models.CharField(max_length=50, verbose_name="Colaborador 1°")
    Colaborador_2 = models.CharField(max_length=50, verbose_name="Colaborador 2°")
    Fotos = models.FileField(upload_to="uploads", max_length=100, null=True, default=None)
    Obs = models.TextField(max_length=500, verbose_name="Observação")
    status_final = models.CharField(max_length=12, choices=Status_final_choices, blank=False, null=False)
    Data_01 = models.DateTimeField('Data da Criação',auto_now_add=True)
    Data_02 = models.DateTimeField('Última atualização', auto_now=True)

    def __str__(self):
        return self.Data_01
    
    
    class Meta:
        verbose_name = "Cadastro De Obras"
        verbose_name_plural = "Cadastros De Obras"
    
   
    # usuario = models.ForeignKey(,
        # User, on_delete=models.PROTECT, verbose_name="usuário")    

    

    def __str__(self):
        return "{} ({})".format(self.DC, self.Colaborador_1)
    
    

class Contatos(models.Model):
    Nome = models.CharField(max_length=20)
    Area = models.CharField(max_length=20, verbose_name='Área')
    Funcao = models.CharField(max_length=20, verbose_name='Função')
    Numero = models.CharField(max_length=20, verbose_name='Número')
    Base = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Contatos"
        verbose_name_plural = "Contatos"

# class Funcionario(models.Model):
#     nome_completo = models.CharField(max_length=100)
#     Ind = models.CharField(max_length=10)
#     cpf = models.CharField(max_length=14, verbose_name="CPF")
#     usuario = models.ForeignKey(
#         User, on_delete=models.PROTECT, verbose_name="usuário")
