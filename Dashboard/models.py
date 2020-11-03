from django.db import models


class DashboardModel(models.Model):
    nombre_com = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_com
    