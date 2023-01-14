

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_asignacion_horarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='hora_fin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='hora_inicio',
            field=models.DateTimeField(),
        ),
    ]
