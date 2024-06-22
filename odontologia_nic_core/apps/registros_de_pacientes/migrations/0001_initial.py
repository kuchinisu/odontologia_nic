# Generated by Django 5.0.6 on 2024-06-18 10:30

import apps.registros_de_pacientes.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=252)),
                ('apellido_materno', models.CharField(max_length=252)),
                ('apellido_paterno', models.CharField(max_length=252)),
                ('correo_electronico', models.CharField(max_length=252)),
                ('direccion', models.CharField(max_length=255)),
                ('nacionalidad', models.CharField(choices=[('mexicana', 'mexicana'), ('estadounidense', 'estadounidense'), ('otro', 'otro')], default='mexicana', max_length=50)),
                ('identificacion_oficial', models.CharField(blank=True, max_length=255)),
                ('genero', models.CharField(choices=[('mujer', 'mujer'), ('hombre', 'hombre'), ('sin especificar', 'sin especificar')], default='sin especificar', max_length=50)),
                ('edad', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estatura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('imc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('id_paciente', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procedimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tratamientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Modelos3DBoca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_archivo', models.IntegerField(unique=True)),
                ('archivo_3d', models.FileField(upload_to=apps.registros_de_pacientes.models.path_dir_models)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelo_3d_del_paciente', to='registros_de_pacientes.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Diente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeracion', models.CharField(choices=[('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85')], max_length=2)),
                ('descripcion', models.TextField()),
                ('documento_de_info', models.FileField(upload_to=apps.registros_de_pacientes.models.path_dir_diente_doc)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diente_del_paciente', to='registros_de_pacientes.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='ProcedimientoRealizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('realizado', models.BooleanField(default=True)),
                ('id_procedimiento', models.IntegerField(unique=True)),
                ('documento', models.FileField(upload_to=apps.registros_de_pacientes.models.path_dir_doc_procedimiento_realizado, default='default/default.txt')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_procedido', to='registros_de_pacientes.paciente')),
                ('procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedimiento_al_paciente', to='registros_de_pacientes.procedimientos')),
            ],
        ),
        migrations.CreateModel(
            name='TratamientoIniciado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('finalizado', models.BooleanField(default=False)),
                ('id_tratamiento', models.IntegerField(unique=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_tratado', to='registros_de_pacientes.paciente')),
                ('documento',models.FileField(upload_to=apps.registros_de_pacientes.models.path_dir_documento_tratamiento_iniciado, default='default/default.txt')),
                ('procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_al_paciente', to='registros_de_pacientes.tratamientos')),
            ],
        ),
        migrations.CreateModel(
            name='TratamientoActualizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('realizado', models.BooleanField(default=True)),
                ('documento',models.FileField(upload_to=apps.registros_de_pacientes.models.path_dir_doc_procedimiento_realizado, default='default/default.txt')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_actualizado', to='registros_de_pacientes.tratamientoiniciado')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_de_informacion', models.FileField(upload_to=apps.registros_de_pacientes.models.path_dir_doc)),
                ('id_aparato', models.IntegerField(unique=True)),
                ('documento',models.FileField(upload_to=apps.registros_de_pacientes.models.path_dir_models, default='default/default.txt')),

                ('aparato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidad_de_aparato', to='registros_de_pacientes.aparato')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='aparatos',
            field=models.ManyToManyField(related_name='aparatos_en_el_paciente', to='registros_de_pacientes.unidad'),
        ),
    ]