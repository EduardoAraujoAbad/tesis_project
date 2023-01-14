

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_auto_20221203_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), (
                    'miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes')], max_length=30)),
                ('hora_inicio', models.DateField()),
                ('hora_fin', models.DateField()),
                ('asignatura', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('horas_asignadas', models.ManyToManyField(to='users.asignacion')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
