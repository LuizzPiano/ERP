from django.db import models
from django.contrib.auth.models import User


def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


def upload_img_obra(instance, filename):
    return f"{instance.DC}-{filename}"


class Obras(models.Model):
    DC = models.CharField(max_length=50)
    Colaborador_1 = models.CharField(max_length=50, verbose_name="Colaborador 1°")
    Colaborador_2 = models.CharField(max_length=50, verbose_name="Colaborador 2°")
    Fotos = models.ImageField(upload_to=upload_img_obra, blank=False, null=True)
    # usuario = models.ForeignKey(
        # User, on_delete=models.PROTECT, verbose_name="usuário")    

    def __str__(self):
        return "{} ({})".format(self.DC, self.Colaborador_1)
    
    

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=100)
    Ind = models.CharField(max_length=10)
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="usuário")
