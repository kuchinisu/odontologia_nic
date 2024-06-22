from django.db import models
from django.utils import timezone
from apps.registros_de_pacientes.models import Paciente
from apps.utils.PathDirs import path_dir_modelo_dental_enviado

class ModeloDentalEnviadoAComparar(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    id_archivo = models.IntegerField(unique=True)
    archivo_3d = models.FileField(upload_to=path_dir_modelo_dental_enviado)

    def get_paciente(self):
        return self.paciente.id_paciente

    def get_archivo_3d(self):
        if self.archivo_3d:
            return str(self.archivo_3d.url)
        return ''
    def save(self, *args, **kwargs):
        modelos = ModeloDentalEnviadoAComparar.objects.all()
        if modelos.exists():
            ultimo_id = modelos.order_by('id_archivo').last().id_archivo + 1
        else:
            ultimo_id = 1
        self.id_archivo = ultimo_id

        super().save(*args, **kwargs)