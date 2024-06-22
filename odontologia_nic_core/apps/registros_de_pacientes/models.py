from django.db import models
from django.utils import timezone
from apps.utils.PathDirs import (path_dir_doc, path_dir_models, path_dir_diente_doc, 
                                 path_dir_doc_procedimiento_realizado, 
                                 path_dir_documento_tratamiento_iniciado,
                                 path_dir_tratamiento_actualizado, 
                                 path_dir_documento_de_afeccion, path_dir_doc_extra_paciente,
                                 path_dir_modelo_3d_unidad)

from apps.utils.globales import (GENEROS, NACIONALIDADES, 
                                 NUMERACION_DE_DIENTES, ESTADOS_DE_AFECCION)

import datetime

class Procedimientos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Tratamientos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Aparato(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Unidad(models.Model):
    aparato = models.ForeignKey(Aparato, on_delete=models.CASCADE, related_name='unidad_de_aparato')
    documento_de_informacion = models.FileField(upload_to=path_dir_doc)
    id_aparato = models.IntegerField(unique=True)
    modelo_3d = models.FileField(upload_to=path_dir_modelo_3d_unidad, default='default/default.txt')
    def __str__(self):
        return f'unidad {self.id_aparato} del aparato {self.aparato}'
    def get_documento(self):
        if self.documento_de_informacion:
            return str(self.documento_de_informacion.url)    
        return ''
    def get_aparato(self):
        if self.aparato:
            return str(self.aparato.nombre)
        return ''
    def save(self, *args, **kwargs):
        unidades = Unidad.objects.all()
        if unidades.exists():
            ultimo_id = unidades.order_by('id_aparato').last().id_aparato + 1
        else:
            ultimo_id = 1
        self.id_aparato = ultimo_id

        super().save(*args, **kwargs)

class Paciente(models.Model):
    nombre=models.CharField(max_length=252)
    apellido_materno=models.CharField(max_length=252)
    apellido_paterno=models.CharField(max_length=252)

    correo_electronico = models.CharField(max_length=252)

    direccion = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=50, choices=NACIONALIDADES, default='mexicana')
    identificacion_oficial = models.CharField(blank=True, max_length=255)
    
    genero = models.CharField(max_length=50, choices=GENEROS, default='sin especificar')
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits = 5, decimal_places = 2)
    estatura = models.DecimalField( max_digits = 3, decimal_places = 2)
    imc = models.DecimalField(max_digits = 5, decimal_places = 2)

    aparatos = models.ManyToManyField(Unidad, related_name='aparatos_en_el_paciente', blank=True)

    id_paciente = models.IntegerField(unique=True)

    fecha_de_nacimiento = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.apellido_paterno} {self.apellido_materno} {self.nombre} {self.id_paciente}'

    def save(self, *args, **kwargs):
        pacientes = Paciente.objects.all()
        if pacientes:
            ultimo_id = pacientes.order_by('id_paciente').last().id_paciente + 1
        else:
            ultimo_id = 1

        self.id_paciente = ultimo_id

        super().save(*args, **kwargs)

class Modelos3DBoca(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='modelo_3d_del_paciente')
    fecha = models.DateTimeField(default=timezone.now)
    id_archivo = models.IntegerField(unique=True)
    archivo_3d = models.FileField(upload_to=path_dir_models)

    def get_paciente(self):
        return self.paciente.id_paciente

    def get_archivo_3d(self):
        if self.archivo_3d:
            return str(self.archivo_3d.url)
        return ''
    def save(self, *args, **kwargs):
        modelos = Modelos3DBoca.objects.all()
        if modelos.exists():
            ultimo_id = modelos.order_by('id_archivo').last().id_archivo + 1
        else:
            ultimo_id = 1
        self.id_archivo = ultimo_id

        super().save(*args, **kwargs)


class Afecciones(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='afecciones_del_paciente')
    descripcion = models.TextField()
    estado = models.CharField(choices=ESTADOS_DE_AFECCION, max_length=40)
    fecha_de_diagnostico = models.DateTimeField(default=timezone.now)
    documento = models.FileField(upload_to=path_dir_documento_de_afeccion)
    id_afeccion = models.IntegerField(default=1)
    def get_paciente(self):
        return self.paciente.id_paciente
    def get_documento(self):
        if self.documento:
            return self.documento.url
        else:
            return ''
    
    def save(self, *args, **kwargs):
        afecciones = Afecciones.objects.all()
        if afecciones.exists():
            ultimo_id = afecciones.order_by('id_afeccion').last().id_afeccion + 1
        else:
            ultimo_id = 1
        self.id_afeccion = ultimo_id

        super().save(*args, **kwargs) 
    
    
class ProcedimientoRealizado(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente_procedido')
    procedimiento = models.ForeignKey(Procedimientos, on_delete=models.CASCADE, related_name='procedimiento_al_paciente')

    fecha = models.DateTimeField(default=timezone.now)
    realizado = models.BooleanField(default=True)
    id_procedimiento = models.IntegerField(unique=True)
    documento = models.FileField(upload_to=path_dir_doc_procedimiento_realizado, default='default/default.txt')

    afeccion = models.ManyToManyField(Afecciones, related_name='afecciones_procedidas', blank=True)

    def __str__(self):
        return f'{self.procedimiento.nombre}: {self.paciente.apellido_paterno} {self.paciente.apellido_materno} {self.paciente.nombre} {self.fecha}'

    def get_paciente(self):
        return self.paciente.id_paciente
    def get_documento(self):
        if self.documento:
            return str(self.documento.url)    
        return ''
    def save(self, *args, **kwargs):
        procedimeintos = ProcedimientoRealizado.objects.all()

        if procedimeintos.exists():
            ultimo_id = procedimeintos.order_by('id_procedimiento').last().id_procedimiento + 1
        else:
            ultimo_id = 1
        
        self.id_procedimiento = ultimo_id

        super().save(*args, **kwargs)

class TratamientoIniciado(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente_tratado')
    procedimiento = models.ForeignKey(Tratamientos, on_delete=models.CASCADE, related_name='tratamiento_al_paciente')

    fecha = models.DateTimeField(default=timezone.now)
    finalizado = models.BooleanField(default=False)
    documento = models.FileField(upload_to=path_dir_documento_tratamiento_iniciado, default='default/default.txt')
    id_tratamiento = models.IntegerField(unique=True)
    afeccion = models.ManyToManyField(Afecciones, related_name='afecciones_tratadas', blank=True)

    def __str__(self):
        return f'{self.procedimiento.nombre}: {self.paciente.apellido_paterno} {self.paciente.apellido_materno} {self.paciente.nombre} {self.fecha}'

    def get_paciente(self):
        return self.paciente.id_paciente
    def get_documento(self):
        if self.documento:
            return str(self.documento.url)    
        return ''
    def save(self, *args, **kwargs):
        tratamientos = TratamientoIniciado.objects.all()
        
        if tratamientos.exists():
            ultimo_id = tratamientos.order_by('id_tratamiento').last().id_tratamiento + 1
        else:
            ultimo_id = 1
        self.id_tratamiento = ultimo_id

        super().save(*args, **kwargs)
    
class TratamientoActualizado(models.Model):
    tratamiento = models.ForeignKey(TratamientoIniciado, on_delete=models.CASCADE, related_name='tratamiento_actualizado')
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    documento = models.FileField(upload_to=path_dir_tratamiento_actualizado, default='default/default.txt')
    realizado = models.BooleanField(default=True)

    def get_tratamiento(self):
        return self.tratamiento.id_tratamiento
    def get_documento(self):
        if self.documento:
            return str(self.documento.url)    
        return ''

class Diente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='diente_del_paciente')
    numeracion =  models.CharField(choices=NUMERACION_DE_DIENTES, max_length=2) 
    descripcion = models.TextField()
    documento_de_info = models.FileField(upload_to=path_dir_diente_doc)
    
    def get_paciente(self):
        return self.paciente.id_paciente
    
    def get_documento(self):
        if self.documento_de_info:
            return str(self.documento_de_info.url)    
        return ''
    
class DocumentoExtraDelPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='documento_del_paciente')
    documento = models.FileField(upload_to=path_dir_doc_extra_paciente)

    def get_paciente(self):
        return self.paciente.id_paciente 
    def get_documento(self):
        if self.documento:
            return str(self.documento.url)    
        return ''
    