from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from users.models import Horarios, Asignacion
#from django.contrib.admin.widgets import AdminDateWidget


class usernameForm(forms.Form):
    username = forms.CharField(max_length=30, label="Nombre de usuario")


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")), label="Fecha")


class UsernameAndDateForm(forms.Form):
    username = forms.CharField(max_length=30, label="Nombre de usuario")
    #course = forms.CharField(max_length=255, label="Asignatura")
    date_from = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")), label="Desde")
    date_to = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")), label="Hasta")


class DateForm_2(forms.Form):
    date_from = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")), label="Desde")
    date_to = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")), label="Hasta")


class Configuracion(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = [
            'user', 'horas_asignadas'
        ]


class Asignacion_Horario(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = [
            'dia', 'hora_inicio', 'hora_fin', 'asignatura'
        ]
        labels = {
            'dia': 'Dias_semana',
            'hora_inicio': 'Hora de Entrada',
            'hora_fin': 'Hora de Salida',
            'asignatura': 'Asignatura'
        }
        widgets = {
            # 'dia': forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, is_hidden=True),
            'hora_inicio': forms.TimeInput(format='%H:%M'),
            'hora_fin': forms.TimeInput(format='%H:%M')
        }
