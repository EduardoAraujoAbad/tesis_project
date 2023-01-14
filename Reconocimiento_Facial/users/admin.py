from django.contrib import admin
from .models import Time, Present, Asignacion, Horarios


# Register your models here.
admin.site.register(Time)
admin.site.register(Present)
admin.site.register(Asignacion)
admin.site.register(Horarios)
