from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import ModeloDentalEnviadoAComparar
from apps.registros_de_pacientes.models import Modelos3DBoca
from apps.utils.math.vertices import comparar_modelos
import tempfile
import requests


class ComparadorModelosModeloDentales(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        usuario_consultando = request.user
        print('--------------------------------\n')
        print('Comparación de modelos 3d\n')
        modelos_3d = Modelos3DBoca.objects.all()
        
        if modelos_3d.exists():
            print('-------------------------------\n')
            print('dentro de la vista\n')

            print('tomando archivo 3d...\n')
            modelo = request.FILES.get('archivo_3d')
            print('archivo tomado\n\n')

            print('registrando el archivo 3d en la base de datos enviado para la comparación...\n')
            nuevo_modelo_enviado = ModeloDentalEnviadoAComparar()
            nuevo_modelo_enviado.archivo_3d = modelo
            nuevo_modelo_enviado.save()
            print('archivo guardado correctamente...\n')
            
            print('recuperando el archivo enviado en la base de datos')
            response_1 = requests.get(f'http://127.0.0.1:8000/media/{nuevo_modelo_enviado.archivo_3d}')
            with tempfile.NamedTemporaryFile(delete=False, suffix='.obj') as send_temp_file:
                    send_temp_file.write(response_1.content)
                    send_temp_model_path = send_temp_file.name

            print('comparacion con cada modelo\n')
            contador = 0
            resultados = []
            for modelo_i in modelos_3d:
                paciente = modelo_i.paciente
                response = requests.get(f'http://127.0.0.1:8000/media/{modelo_i.archivo_3d}')
                with tempfile.NamedTemporaryFile(delete=False, suffix='.obj') as remote_temp_file:
                    remote_temp_file.write(response.content)
                    remote_temp_model_path = remote_temp_file.name

                resultados.append(
                    {   
                        'paciente':{
                             'apellido paterno':paciente.apellido_paterno,
                             'apellido materno':paciente.apellido_materno,
                             'nombre':paciente.nombre,
                             'genero':paciente.genero,
                             'fecha de nacimiento':paciente.fecha_de_nacimiento,
                             'estatura':paciente.estatura,
                             'peso':paciente.peso,
                             'direccion':paciente.direccion,
                             'identifiacion oficial':paciente.identificacion_oficial if paciente.identificacion_oficial else None,
                             'identificacion del paciente':paciente.id_paciente,
                        }, 
                        'resultado':comparar_modelos(send_temp_model_path, remote_temp_model_path)
                    }
                      )
                contador+=1
                print(f'comparacion: {contador} lista\n')

            return Response({'mensaje':resultados}) 
    