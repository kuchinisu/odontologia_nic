from django.contrib import admin
from .models import (
    Procedimientos, Tratamientos, Aparato, Unidad, Paciente, Modelos3DBoca, 
    ProcedimientoRealizado, TratamientoIniciado, TratamientoActualizado, Diente, Afecciones
)

admin.site.register(Procedimientos)
admin.site.register(Tratamientos)
admin.site.register(Aparato)
admin.site.register(Unidad)
admin.site.register(Paciente)
admin.site.register(Modelos3DBoca)
admin.site.register(ProcedimientoRealizado)
admin.site.register(TratamientoIniciado)
admin.site.register(TratamientoActualizado)
admin.site.register(Diente)
admin.site.register(Afecciones)
