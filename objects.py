from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

def create_triangle(program, x, y, scale, rotation, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui

    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (+0.0, +0.0),
        (+0.1, +0.2),
        (+0.2, +0.0),
    ]

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_nose(program, x, y, scale, rotation, R, G, B, mode):
    
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

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_mouth(program, x, y, scale, rotation, R, G, B, mode):
    
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

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_head(program, x, y, scale, rotation, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui
    
    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (+0.0, +0.65),
        (+0.3, +0.0),
        (-0.3, +0.0),
        (+0.0, -0.45),
    ]

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_hair(program, x, y, scale, rotation, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui
    
    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (0.270, -0.200),
        (0.225, -0.250),
        (0.268, -0.279),
        (0.341, -0.164),
        (0.300, -0.182),
        (0.309, -0.108),
        (0.285, -0.042),
        (0.263, -0.122),
        (0.200, -0.066),
        (0.127, -0.048),
        (0.063, -0.048),
        (0.127, -0.090),
        (0.158, -0.130),
        (0.066, -0.154),
        (0.140, -0.188),
        (0.084, -0.244),
        (0.170, -0.243),
        (0.225, -0.250),
    ]

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_hair_outline(program, x, y, scale, rotation, R, G, B, mode):
    
    # Funcao para calcular os vertices aqui
    
    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (0.225, -0.250),
        (0.268, -0.279),
        (0.341, -0.164),
        (0.300, -0.182),
        (0.309, -0.108),
        (0.285, -0.042),
        (0.263, -0.122),
        (0.200, -0.066),
        (0.127, -0.048),
        (0.063, -0.048),
        (0.127, -0.090),
        (0.158, -0.130),
        (0.066, -0.154),
        (0.140, -0.188),
        (0.084, -0.244),
        (0.170, -0.243),
    ]

    return [vertices, x, y, scale, rotation, R, G, B, mode]