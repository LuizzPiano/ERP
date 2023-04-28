from django.db import models
from django.contrib.auth.models import User


tipo_carros = (
        ("Agregado", "Agregado"),
        ("Icomon", "Icomon"),
        ("Parceiro", "Parceiro")
    )


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    ind = models.CharField(max_length=20, verbose_name="ID")
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    veiculo = models.CharField(max_length=100, help_text="Modelo do veiculo")
    Cor = models.CharField(max_length=20)
    Placa = models.CharField(max_length=20)
    Tipo_veiculo = models.CharField(max_length=22, choices=tipo_carros, blank=False, null=False)


    class Meta:
        verbose_name = "Coladorador"
        verbose_name_plural = "Colaboradores"


    def __str__(self):
        return self.nome_completo
