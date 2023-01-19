from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.


class Present(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time = models.DateTimeField(null=True, blank=True)
    present = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %s  %s %s  %s" % (self.id, self.user, self.date, self.time, self.present)


class Time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time = models.DateTimeField(null=True, blank=True)
    out = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %s  %s  %s %s" % (self.id, self.user, self.date, self.time, self.out)


class Asignacion(models.Model):
    dia_semana = [('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles',
                                                             'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes')]
    dia = models.CharField(max_length=30, choices=dia_semana)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    asignatura = models.CharField(max_length=255)

    def __str__(self):
        return self.dia.capitalize()+':'+" ["+str(self.asignatura)+"("+str(self.hora_inicio)+" - "+str(self.hora_fin)+")"+"]"


class Horarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    horas_asignadas = models.ManyToManyField(Asignacion, related_name="horas")

    def __str__(self):
        return "%s: %s  %s " % (self.id, self.user, self.horas_asignadas)

