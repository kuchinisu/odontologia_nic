import os
import uuid

def path_dir_doc(instance, filename):
    ext = filename.split('.')[-1]
    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    
    aparato = instance.aparato.nombre
    id_unidad = str(instance.id_aparato)

    ruta_completa = os.path.join('documentos', aparato, id_unidad, nombre_archivo)

    print(ruta_completa)  
    return ruta_completa

def path_dir_models(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    paciente = str(instance.paciente.id_paciente)
    id_archivo = str(instance.id_archivo)
    ruta_completa = os.path.join(paciente, 'modelos', id_archivo, nombre_archivo)
    print(ruta_completa)
    return ruta_completa

def path_dir_modelo_dental_enviado(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    id_archivo = str(instance.id_archivo)
    ruta_completa = os.path.join('modelos_3d', 'bocales_enviados_a_comparar', id_archivo, nombre_archivo)
    print(ruta_completa)
    return ruta_completa



def path_dir_diente_doc(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    paciente = str(instance.paciente.id_paciente)
    numero = str(instance.numeracion)
    ruta_completa = os.path.join(paciente, 'dientes', numero, nombre_archivo)
    print(ruta_completa)
    return ruta_completa

def path_dir_doc_procedimiento_realizado(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    paciente = str(instance.paciente.id_paciente)
    fecha = str(instance.fecha).replace(' ','_').replace(':','_').replace('.','_').replace('+','_')
    ruta_completa = os.path.join(paciente, 'procedimientos', fecha, nombre_archivo)
    
    print(ruta_completa)
    return ruta_completa

def path_dir_documento_tratamiento_iniciado(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    paciente = str(instance.paciente.id_paciente)
    fecha = str(instance.fecha).replace(' ','_').replace(':','_').replace('.','_').replace('+','_')
    ruta_completa = os.path.join(paciente, 'tratamientos', 'iniciados',  fecha, nombre_archivo)

    print(ruta_completa)
    return ruta_completa

def path_dir_tratamiento_actualizado(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    paciente = instance.paciente.id_paciente
    fecha = str(instance.fecha).replace(' ','_').replace(':','_').replace('.','_').replace('+','_')
    ruta_completa = os.path.join(paciente, 'tratamientos', 'actualizados',  fecha, nombre_archivo)

    print(ruta_completa)
    return ruta_completa

def path_dir_documento_de_afeccion(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    paciente = str(instance.paciente.id_paciente)
    fecha = str(instance.fecha_de_diagnostico).replace(' ','_').replace(':','_').replace('.','_').replace('+','_')
    ruta_completa = os.path.join( paciente, 'afecciones',  fecha, nombre_archivo)

    print(ruta_completa)
    return ruta_completa

def path_dir_doc_extra_paciente(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    paciente = str(instance.paciente.id_paciente)
    fecha = str(instance.fecha).replace(' ','_').replace(':','_').replace('.','_').replace('+','_')
    ruta_completa = os.path.join(paciente, 'extra_docs',  fecha, nombre_archivo)

    print(ruta_completa)
    return ruta_completa

def path_dir_modelo_3d_unidad(instance, filename):
    ext = filename.split('.')[-1]

    nombre_archivo = f"{uuid.uuid4()}.{ext}"
    
    aparato = instance.aparato.nombre
    unidad = str(instance.id_aparato)

    ruta_completa = os.path.join('modelos_3d', aparato, unidad, nombre_archivo)
    

    print(ruta_completa)
    return ruta_completa