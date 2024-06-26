# Generated by Django 5.0.6 on 2024-06-18 20:42

import apps.utils.PathDirs
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros_de_pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamientoactualizado',
            name='documento',
            field=models.FileField(default='default/default.txt', upload_to=apps.utils.PathDirs.path_dir_tratamiento_actualizado),
        ),
        migrations.CreateModel(
            name='Afecciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('vigente sin tratamiento', 'vigente sin tratamiento'), ('en tratamiento', 'en tratamiento'), ('tratamiento terminado', 'tratamiento terminado'), ('tratamiento suspendido', 'tratamiento suspendido'), ('irrebersible con intento de tratamiento', 'irrebersible con intento de tratamiento'), ('irrebersible sin intento de tratamiento', 'irrebersible sin intento de tratamiento')], max_length=40)),
                ('fecha_de_diagnostico', models.DateTimeField(default=django.utils.timezone.now)),
                ('documento', models.FileField(upload_to=apps.utils.PathDirs.path_dir_documento_de_afeccion)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='afecciones_del_paciente', to='registros_de_pacientes.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='procedimientorealizado',
            name='afeccion',
            field=models.ManyToManyField(blank=True, related_name='afecciones_procedidas', to='registros_de_pacientes.afecciones'),
        ),
        migrations.AddField(
            model_name='tratamientoiniciado',
            name='afeccion',
            field=models.ManyToManyField(blank=True, related_name='afecciones_tratadas', to='registros_de_pacientes.afecciones'),
        ),
        migrations.CreateModel(
            name='DocumentoExtraDelPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.FileField(upload_to=apps.utils.PathDirs.path_dir_doc_extra_paciente)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documento_del_paciente', to='registros_de_pacientes.paciente')),
            ],
        ),
    ]
