from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

def create_triangle(program, x, y, rotation, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui

    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (+0.0, +0.0),
        (+0.1, +0.2),
        (+0.2, +0.0),
    ]

    return [vertices, x, y, rotation, R, G, B, mode]

def create_nose(program, x, y, rotation, R, G, B, mode):
    
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

    return [vertices, x, y, rotation, R, G, B, mode]

def create_mouth(program, x, y, rotation, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui

    num_vertices = 32 # define a "qualidade" do circulo
    pi = 3.14
    counter = 0
    radius = 0.5
    vertices = []

    angle = 0.0
    for counter in range(num_vertices):
        angle += 2*pi/num_vertices 
        x = math.cos(angle)*radius
        y = math.sin(angle)*radius
        # x = np.float64(round(x, 3))
        # y = np.float64(round(y, 3))
        
        # Para pegar somente o semi circulo inferior, ignore os primeiros 15 pontos
        if counter > 14:
            vertices.append((x,y))

    return [vertices, x, y, rotation, R, G, B, mode]