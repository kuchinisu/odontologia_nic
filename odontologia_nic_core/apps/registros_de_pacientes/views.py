from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
import datetime
from .models import (Paciente, Procedimientos, Tratamientos, Aparato, Unidad, Modelos3DBoca, 
                     Afecciones, ProcedimientoRealizado, TratamientoIniciado, TratamientoActualizado, Diente, DocumentoExtraDelPaciente,
                     Aparato)
import numpy as np
from django.http import Http404

from rest_framework.permissions import IsAuthenticated
import json

from apps.utils.paginator import LargeSetPagination, SmallSetPagination, MediumSetPagination
from .serializer import (
    PacienteSerializer, TratamientoSerializer, AparatoSerializer, UnidadSerializer, 
    Modelos3DSerializer, AfeccionesSerializer, ProcedimientoRealizadoSerializer, 
    TratamientoIniciadoSerializer, TratamientoActualizadoSerializer, DienteSerializer, 
    DocumentoExtraSerializer,
)
from apps.utils.math.calculos import calcular_edad

from apps.utils.minis_f import str_a_bool
from apps.utils.globales import KEYS_PRINCIPALES

"""
posts
""" 
class RegistrarModeloDeBoca(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        data = request.data

        paciente_ = data.get('paciente')
        paciente = get_object_or_404(Paciente, id_paciente = paciente_)

        nuevo_modelo_3d = Modelos3DBoca(
            paciente = paciente,
        )

        archivo_3d = request.FILES.get('archivo_3d')

        nuevo_modelo_3d.archivo_3d = archivo_3d

        nuevo_modelo_3d.save()

        return Response({'mensaje':'nuevo modelo 3d registrado correctamente'}, status=status.HTTP_201_CREATED)

class RegistrarPaciente(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        pass
    def post(self,request, format=None):
        data = request.data
        nombre = data.get('nombre')
        apellido_materno = data.get('apellido_materno')
        apellido_paterno = data.get('apellido_paterno')

        correo_electronico = data.get('correo_electronico')
        direccion = data.get('direccion')
        nacionalidad = data.get('nacionalidad')
        identificacion_oficial = data.get('identificacion_oficial')
        genero = data.get('genero')

        
        peso = data.get('peso')
        estatura = data.get('estatura')
        
        fecha_de_nacimiento = str(data.get('fecha_de_nacimiento')).replace('-','/')
        fecha_de_nacimiento_dt = datetime.datetime.strptime(fecha_de_nacimiento, '%Y/%m/%d')
        edad = calcular_edad(fecha_de_nacimiento_dt)
        fecha_de_nacimiento_aware = timezone.make_aware(fecha_de_nacimiento_dt)

        imc = float(peso) / np.power(float(estatura), 2)

        nuevo_paciente = Paciente(
            nombre=nombre,
            apellido_materno = apellido_materno,
            apellido_paterno = apellido_paterno,
            correo_electronico = correo_electronico,
            direccion = direccion,
            nacionalidad = nacionalidad,
            genero = genero,
            edad = int(edad),
            peso = peso,
            imc = imc,
            estatura = estatura,
            fecha_de_nacimiento = fecha_de_nacimiento_aware,
        )

        if identificacion_oficial:
            nuevo_paciente.identificacion_oficial = identificacion_oficial

        nuevo_paciente.save()

        return Response({'mensaje':'paciente registrado correctamente'}, status=status.HTTP_201_CREATED)
    

class RegistrarProcedimiento(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, fromat=None):
        pass
    def post(self, request, format=None):
        data = request.data

        nombre = data.get('nombre')
        descripcion = data.get('descripcion')

        nuevo_procedimiento = Procedimientos(
            nombre = nombre,
            descripcion = descripcion,
        )

        nuevo_procedimiento.save()

        return Response({'mensaje':'procedimiento registrado correctamente'}, status=status.HTTP_201_CREATED)
    
class RegistrarTratamiento(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, fromat=None):
        pass
    def post(self, request, format=None):
        data = request.data

        nombre = data.get('nombre')
        descripcion = data.get('descripcion')

        nuevo_tratamiento = Tratamientos(
            nombre = nombre,
            descripcion = descripcion,
        )

        nuevo_tratamiento.save()

        return Response({'mensaje':'trtamiento registrado correctamente'}, status=status.HTTP_201_CREATED)
    
class RegistrarAparato(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, fromat=None):
        pass
    def post(self, request, format=None):
        data = request.data

        nombre = data.get('nombre')

        nuevo_aparato = Aparato(
            nombre = nombre,
        )

        nuevo_aparato.save()

        return Response({'mensaje':'aparato registrado correctamente'}, status=status.HTTP_201_CREATED)
    
class RegistrarUnidad(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, fortmat=None):
        pass
    def post(self, request, format=None):
        data = request.data
        aparato_n = data.get('aparato')

        aparato = get_object_or_404(Aparato, nombre=aparato_n)
        documento_de_informacion = request.FILES.get('documento_de_informacion')
        matriz_3d = request.FILES.get('modelo_3d')

        nueva_unidad = Unidad(
            aparato = aparato,
        )

        nueva_unidad.documento_de_informacion = documento_de_informacion
        nueva_unidad.modelo_3d = matriz_3d
        nueva_unidad.save()

        return Response({'mensaje':'unidad regisitrada correctamente'}, status=status.HTTP_201_CREATED)

class RegistrarAfeccion(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, format= None):
        pass
    def post(self, request, format=None):
        data = request.data

        paciente_n = data.get('paciente')
        paciente = get_object_or_404(Paciente, id_paciente=paciente_n)

        descripcion = data.get('descripcion')
        
        estado = data.get('estado')

        documento = request.FILES.get('documento')

        nueva_afeccion = Afecciones(
            paciente = paciente,
            descripcion = descripcion,
            estado = estado,

        )

        if data.get('fecha_de_diagnostico'):
            fecha_ = data.get('fecha_de_diagnostico')
            nueva_afeccion.fecha_de_diagnostico = fecha_
        
        nueva_afeccion.documento = documento

        nueva_afeccion.save()

        return Response({'mensaje':f'afeccion al paciente {paciente.nombre} {paciente.apellido_paterno} {paciente.apellido_materno} - ({paciente.id_paciente}) registrada correctamente'}, 
                        status=status.HTTP_201_CREATED)

class RegistrarProcedimientoRealizado(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        pass
    def post(self, request, format=None):
        data = request.data

        paciente_ = data.get('paciente')
        paciente = get_object_or_404(Paciente, id_paciente=paciente_)

        procedimiento_ = data.get('procedimiento')
        procedimiento = get_object_or_404(Procedimientos, nombre = procedimiento_)

        realizado = str_a_bool(data.get('realizado'))

        nuevo_procedimiento_realizado = ProcedimientoRealizado(
            paciente = paciente,
            procedimiento = procedimiento,
            realizado = realizado,

        )

        if data.get('afecciones'):
            afecciones = json.loads(data.get('afecciones'))

            for afeccion_n in afecciones:
                try:
                    afeccion = get_object_or_404(Afecciones, id_afeccion=afeccion_n)
                    nuevo_procedimiento_realizado.afeccion.add(afeccion)

                except Http404 as e:
                    continue


        documento = request.FILES.get('documento')
        nuevo_procedimiento_realizado.documento = documento

        nuevo_procedimiento_realizado.save()

        return Response({'mensaje':'procedimiento realizado registrado correctamente'}, status=status.HTTP_201_CREATED)
    
class RegistrarTratamientoIniciado(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        pass
    def post(self, request, format=None):
        data = request.data 

        paciente_ = data.get('paciente')
        paciente = get_object_or_404(Paciente, id_paciente=paciente_)

        tratamiento_ = data.get('tratamiento')
        tratamiento = get_object_or_404(Tratamientos, nombre = tratamiento_)

        #finalizado = data.get('finalizado')

        nuevo_tratamiento_iniciado = TratamientoIniciado(
            paciente = paciente,
            procedimiento = tratamiento,
            finalizado = False,
        )

        if data.get('afecciones'):
            afecciones = json.loads(data.get('afecciones'))
            nuevo_tratamiento_iniciado.save()

            for afeccion_ in afecciones:
                try:
                    afeccion = get_object_or_404(Afecciones, id_afeccion=afeccion_, paciente=paciente)
                    nuevo_tratamiento_iniciado.afeccion.add(afeccion)
                except Http404 as e:
                    print(f'{afeccion_} no existe: {e}')
        
        documento = request.FILES.get('documento')

        nuevo_tratamiento_iniciado.documento = documento

        nuevo_tratamiento_iniciado.save()

        return Response({'mensaje':'nuevo tratamiento iniciado registrado correctamente'}, status=status.HTTP_201_CREATED)
    
class RegistrarTratamientoActualizado(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        pass
    def post(self, request, format=None):
        data = request.data 

        tratamiento_ = data.get('tratamiento')
        tratamiento = get_object_or_404(TratamientoIniciado, id_tratamiento = tratamiento_)

        descripcion = data.get('descripcion')
        realizado = data.get('descripcion')
        nuevo_tratamiento_actualizado = TratamientoActualizado(
            tratamiento = tratamiento,
            descripcion=descripcion,
            realizado = True,
        )

        if data.get('fecha'):
           fecha = data.get('fecha')
           nuevo_tratamiento_actualizado.fecha = fecha

        documento = request.FILES.get('documento')

        nuevo_tratamiento_actualizado.documento = documento

        nuevo_tratamiento_actualizado
        
        return Response({'mensaje':'actualizacion de tratamiento registrado correctamente'}, status=status.HTTP_201_CREATED)
    

class RegistrarDiente(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        data = request.data

        paciente_=data.get('paciente')
        paciente = get_object_or_404(Paciente, id_paciente=paciente_)

        numeracion = data.get('numeracion')

        descripcion = data.get('descripcion')


        nuevo_diente = Diente(
            paciente = paciente,
            numeracion = str(numeracion),
            descripcion = descripcion,
            
        )

        documento = request.FILES.get('documento')

        nuevo_diente.documento_de_info = documento

        nuevo_diente.save()

        return Response({'mensaje':'diente registrado correctamente'}, status=status.HTTP_201_CREATED)
    
class DocExtra(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, format= None):
        pass

    def post(self, request, format=None):
        data = request.data

        paciente_ = data.get('paciente')
        paciente = get_object_or_404(Paciente, id_paciente=paciente_)

        nuevo_doc = DocumentoExtraDelPaciente(
            paciente = paciente,
        )

        doc = data.get('doc')

        nuevo_doc.documento = doc

        nuevo_doc.save()

        return Response({'mensaje':'nuevo documento guardado correctamente'}, status=status.HTTP_201_CREATED)
    
"""
    gets
"""
#edad__gte
#edad__lte

class BuscarPacientesPorParametros(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        #data = request.data
        
        pacientes = Paciente.objects.filter(**kwargs)

        if pacientes.exists():

            paginator = LargeSetPagination()

            results = paginator.paginate_queryset(pacientes, request)
            serializer = PacienteSerializer(results, many=True)
            
            return paginator.get_paginated_response({'pacientes':serializer.data})
        else:
            return Response({'error':'no hay pacientes que encajen con los filtros'}, status=status.HTTP_404_NOT_FOUND)

        

class GetPacientes(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        pacientes = Paciente.objects.all().order_by('id_paciente')

        if pacientes:
            paginator = LargeSetPagination()

            results = paginator.paginate_queryset(pacientes, request)
            serializer = PacienteSerializer(results, many=True)

            return paginator.get_paginated_response({'pacientes':serializer.data})
        else:
            return Response({'error':'no hay pacientes registrados'}, status=status.HTTP_404_NOT_FOUND)
        
class GetPaciente(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id_paciente, format=None):
        pacientes = Paciente.objects.filter(id_paciente=id_paciente)

        if pacientes:
            paginator = LargeSetPagination()

            results = paginator.paginate_queryset(pacientes, request)
            serializer = PacienteSerializer(results, many=True)

            return paginator.get_paginated_response({'pacientes':serializer.data})
        else:
            return Response({'error':f'el paciente {id_paciente} no fue encontrado en la base de datos'}, status=status.HTTP_404_NOT_FOUND)

class GetAfecciones(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, id_paciente, format=None):
        paciente = get_object_or_404(Paciente, id_paciente=id_paciente)

        afecciones = Afecciones.objects.all()
        if afecciones.exists():
            paginator = LargeSetPagination()
            results = paginator.paginate_queryset(afecciones, request)
            serializer = AfeccionesSerializer(results, many=True)

            return paginator.get_paginated_response({'afecciones':serializer.data})
        else:
            Response({'error':f'el paciente {paciente.id_paciente} no tiene afecciones registradas en la base de datos'}, status=status.HTTP_404_NOT_FOUND)

class GetProcedimientosRealizados(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, id_paciente, format=None):
        paciente = get_object_or_404(Paciente, id_paciente=id_paciente)

        procedimientos = ProcedimientoRealizado.objects.all()
        if procedimientos.exists():
            paginator = LargeSetPagination()
            results = paginator.paginate_queryset(procedimientos, request)
            serializer = ProcedimientoRealizadoSerializer(results, many=True)

            return paginator.get_paginated_response({'procedimientos_realizados':serializer.data})
        else:
            Response({'error':f'no hay registros de procedimientos realizados en el paciente {paciente.id_paciente}'}, status=status.HTTP_404_NOT_FOUND)

class GetTratamientosIniciados(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, id_paciente, format=None):
        paciente = get_object_or_404(Paciente, id_paciente=id_paciente)

        tratamientos = TratamientoIniciado.objects.all()
        if tratamientos.exists():
            paginator = LargeSetPagination()
            results = paginator.paginate_queryset(tratamientos, request)
            serializer = TratamientoIniciadoSerializer(results, many=True)

            return paginator.get_paginated_response({'tratamientos_iniciados':serializer.data})
        else:
            Response({'error':f'no hay registros de tratamientos iniciados en el paciente {paciente.id_paciente}'}, status=status.HTTP_404_NOT_FOUND)


class GetTratamientosActualizados(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, id_tratamiento, format=None):
        tratamiento = get_object_or_404(TratamientoIniciado, id_tratamiento=id_tratamiento)
        
        tratamientos = TratamientoActualizado.objects.filter(tratamiento=tratamiento)
        if tratamientos.exists():
            paginator = LargeSetPagination()
            results = paginator.paginate_queryset(tratamientos, request)
            serializer = TratamientoActualizadoSerializer(results, many=True)

            return paginator.get_paginated_response({'tratamientos_actualizados':serializer.data})
        else:
            Response({'error':
                      f'no hay registros de seguimientos del tratamiento con el id {tratamiento.id_tratamiento} en el paciente {tratamiento.paciente.id_paciente} - {tratamiento.paciente.apellido_paterno} {tratamiento.paciente.apellido_materno} {tratamiento.paciente.nombre}'}, 
                      status=status.HTTP_404_NOT_FOUND)


class GetDientes(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, id_paciente, format=None):
        paciente = get_object_or_404(Paciente, id_paciente=id_paciente)

        dientes = Diente.objects.filter(paciente=paciente)
        if dientes.exists():
            paginator = LargeSetPagination()
            results = paginator.paginate_queryset(dientes, request)
            serializer = DienteSerializer(results, many=True)

            return paginator.get_paginated_response({'tratamientos_actualiz':serializer.data})
        else:

            Response({'error':f'los dientes del paciente {paciente.id_paciente}-{paciente.apellido_paterno} {paciente.apellido_materno} {paciente.apellido_materno} no han sido registrados en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
