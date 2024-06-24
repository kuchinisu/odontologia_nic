from django.urls import path
from .views import *

urlpatterns = [ 
    path('registrar/modelo_3d_boca/', RegistrarModeloDeBoca.as_view()),
    path('registrar/paciente/', RegistrarPaciente.as_view()),
    path('registrar/procedimiento/', RegistrarProcedimiento.as_view()),
    path('registrar/tratamiento/', RegistrarTratamiento.as_view()),
    path('registrar/aparato/', RegistrarAparato.as_view()),
    path('registrar/unidad/', RegistrarUnidad.as_view()),
    path('registrar/afeccion/', RegistrarAfeccion.as_view()),
    path('registrar/procedimiento_realizado/', RegistrarProcedimientoRealizado.as_view()),
    path('registrar/tratamiento_iniciado/', RegistrarTratamientoIniciado.as_view()),
    path('registrar/actualizacion_de_tratamiento/', RegistrarTratamientoActualizado.as_view()),
    path('registrar/diente/', RegistrarDiente.as_view()),
    path('registrar/doc_extra/', DocExtra.as_view()),
    
    path('consultar/pacientes/parametros/', BuscarPacientesPorParametros.as_view()),
    path('consultar/pacientes/', GetPacientes.as_view()),
    path('consultar/pacientes/<id_paciente>/', GetPaciente.as_view()),
    path('consultar/afecciones/<id_paciente>/', GetAfecciones.as_view()),
    path('consultar/procedimientos_realizados/<id_paciente>/', GetProcedimientosRealizados.as_view()),
    path('consultar/tratamientos_iniciados/<id_paciente>/', GetTratamientosIniciados.as_view()),
    path('consultar/tratamientos_actualizados/<id_tratamiento>/', GetTratamientosActualizados.as_view()),
    path('consultar/dientes/<id_paciente>/', GetDientes.as_view()),
]
