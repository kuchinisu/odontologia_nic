import trimesh
import numpy as np

import tempfile

def combinar_mallas(mallas, n):
    print('----------------------------------------"\n')
    print('dentro de "combinar_mallas"\n')
    print(f'cantidad de mallas a combinar: {len(mallas)} del archivo {n}\n')
    if len(mallas) == 1:
        return mallas[0]
    return trimesh.util.concatenate(mallas)

def reordenar_vertices(vertices):
    distances = np.linalg.norm(vertices, axis=1)
    sorted_indices = np.argsort(distances)
    reordered_vertices = vertices[sorted_indices]
    return reordered_vertices, sorted_indices

def update_faces(faces, sorted_indices):
    index_mapping = {old_idx: new_idx for new_idx, old_idx in enumerate(sorted_indices)}
    updated_faces = np.vectorize(index_mapping.get)(faces)
    return updated_faces

def cargar_malla(model_path, n):
    print('----------------------------------------"\n')
    print('dentro de la funcion "cargar_malla"\n')
    try:
        mesh = trimesh.load(model_path)
        print(f'cargando archivo {n}.... tipo de instancia: {type(mesh)}\n')
        if isinstance(mesh, trimesh.Scene):
            mesh = combinar_mallas(list(mesh.geometry.values()), n)
        else:
            print(f'vertices de la malla del archivo {n}: {mesh.vertices.size}')
        return mesh
    except Exception as e:
        raise ValueError(f"Error cargando la malla de {model_path}: {e}")

def comparar_modelos(model_path1, model_path2):

    print('----------------------------------------"\n')
    print('dentro de la funcion "comparar_modelos"\n')

    print('cargando malla 1\n')
    mesh1 = cargar_malla(model_path1, 1)

    print('----------------------------------------"\n')
    print('de regreso en"comparar_modelos"\n')

    print('cargando malla 2\n')
    mesh2 = cargar_malla(model_path2, 2)
    print('----------------------------------------"\n')
    print('de regreso en"comparar_modelos"\n')

    if mesh1 is None or mesh2 is None:
        raise ValueError("Una de las mallas es None")

    vertices1, faces1 = mesh1.vertices, mesh1.faces
    vertices2, faces2 = mesh2.vertices, mesh2.faces
    print(vertices1.size)
    if vertices1.size == 0 or vertices2.size == 0:
        raise ValueError("Una de las mallas no tiene vértices.")

    print('Reordenando vértices....')
    reordered_vertices1, sorted_indices1 = reordenar_vertices(vertices1)
    reordered_vertices2, sorted_indices2 = reordenar_vertices(vertices2)
    print('Vértices reordenados....')

    print('Actualizando caras....')
    updated_faces1 = update_faces(faces1, sorted_indices1)
    updated_faces2 = update_faces(faces2, sorted_indices2)
    print('Caras actualizadas....')

    print('Comparando vértices....')
    vertices_equal = np.allclose(reordered_vertices1, reordered_vertices2)
    faces_equal = np.array_equal(updated_faces1, updated_faces2)
    print('Comparación lista')

    return vertices_equal and faces_equal
