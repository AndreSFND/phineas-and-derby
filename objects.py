from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

def create_triangle(program, x, y, rotation, R, G, B, mode):
    
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
        (-0.05, +0.0),
        (+0.1, +0.1),
        (+0.2, +0.3),
        (+0.3, +0.2),
        (+0.4, +0.4),
        (+0.5, +0.25),
        (+0.6, +0.4),
        (+0.7, +0.2),
        (+0.8, +0.3),
        (+0.9, +0.1),
        (+1.05, +0.0),
    ]

    return [vertices, x, y, R, G, B, mode]
