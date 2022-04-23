from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

def create_triangle(program, x, y, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui

    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (+0.0, +0.0),
        (+0.1, +0.2),
        (+0.2, +0.0),
    ]

    return [vertices, x, y, R, G, B, mode]

def create_nose(program, x, y, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui
    
    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (+0.0, +0.0),
        (+0.1, +0.2),
        (+0.2, +0.0),
    ]

    return [vertices, x, y, R, G, B, mode]