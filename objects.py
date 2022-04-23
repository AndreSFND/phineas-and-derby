from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

from utils import upload_data

def create_triangle(program):
    
    # Inicializa as coordenadas do objeto
    x = 0
    y = 0

    # Inicializa as cores do objeto
    R = 0.0
    G = 0.0
    B = 1.0

    # Preparando espaço para 3 vertices usando 2 coordenadas (x,y)
    vertices = np.zeros(3, [("position", np.float32, 2)])

    # Preenchendo as coordenadas de cada vértice
    vertices['position'] = [
                                (+0.1, +0.2),
                                (+0.0, +0.0),
                                (+0.2, +0.0)
                            ]

    upload_data(program, vertices)

    return [vertices, x, y, R, G, B]