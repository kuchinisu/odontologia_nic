from rest_framework import serializers
from .models import (Procedimientos, Tratamientos, Aparato, Unidad, Paciente,
                     Modelos3DBoca, Afecciones, ProcedimientoRealizado, TratamientoIniciado, 
                     TratamientoActualizado, Diente, DocumentoExtraDelPaciente
                     )

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimientos
        fields = [
            'nombre',
            'descripcion',
        ]
class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamientos
        fields = [
            'nombre',
            'descripcion',
        ]

class AparatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aparato
        fields = [
            'nombre',
        ]

class UnidadSerializer(serializers.ModelSerializer):
    documento_de_informacion = serializers.CharField(source='get_documento')
    aparato = serializers.CharField(source='get_aparato')
    class Meta:
        model = Unidad
        fields = [
            'aparato',
            'documento_de_informacion',
            'id_aparato',
        ]

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido_materno',
            'apellido_paterno',
            'correo_electronico',
            'direccion',
            'nacionalidad',
            'identificacion_oficial',
            'genero',
            'edad',
            'peso',
            'estatura',
            'imc',
            'aparatos',
            'id_paciente',
        ]

class Modelos3DSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='get_paciente')
    archivo_3d = serializers.CharField(source='get_archivo_3d')
    class Meta:
        model = Modelos3DBoca
        fields = [
            'paciente',
            'fecha',
            'id_archivo',
            'archivo_3d',
        ]

class AfeccionesSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='get_paciente')
    documento = serializers.CharField(source='get_documento')

    class Meta:
        model = Afecciones

        fields=[
            'paciente',
            'descripcion',
            'estado',
            'fecha_de_diagnostico',
            'documento',
        ]

class ProcedimientoRealizadoSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='get_paciente')
    documento = serializers.CharField(source='get_documento')
    class Meta:
        model = ProcedimientoRealizado
        fields = [
            'paciente',
            'procedimiento',
            'fecha',
            'realizado',
            'id_procedimiento',
            'documento',
            'afeccion',
        ]

class TratamientoIniciadoSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='get_paciente')
    documento = serializers.CharField(source='get_documento')

    class Meta:
        model = TratamientoIniciado
        fields=[
            'paciente',
            'procedimiento',
            'fecha',
            'documento',
            'finalizado',
            'id_tratamiento',
            'afeccion',
        ]

class TratamientoActualizadoSerializer(serializers.ModelSerializer):
    tratamiento = serializers.CharField(source='get_tratamiento')
    documento = serializers.CharField(source='get_documento')

    class Meta:
        model = TratamientoActualizado
        fields = [
            'tratamiento',
            'description',
            'fecha',
            'documento',
            'realizado',

        ]

class DienteSerializer(serializers.ModelSerializer):
    documento_de_info = serializers.CharField(source='get_documento')

    class Meta:
        model = Diente
        fields = [
            'paciente',
            'numeracion',
            'documento_de_info',
        ]

class DocumentoExtraSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='get_paciente')
    documento = serializers.CharField(source='get_documento')

    class Meta:
        model = DocumentoExtraDelPaciente
        fields=[
            'paciente',
            'documento',
        ]