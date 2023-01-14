

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_asignacion_hora_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='hora_fin',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]
