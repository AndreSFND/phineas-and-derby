from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

def create_triangle(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
    # Funcao para calcular os vertices aqui

    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (-0.1, +0.0),
        (+0.1, +0.0),
        (+0.0, +0.14),
    ]

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_nose(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
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

def create_mouth(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
    # Funcao para calcular os vertices aqui

    num_vertices = 32 # define a "qualidade" do circulo
    pi = 3.14
    counter = 0
    radius = 0.5
    vertices = []

    angle = 0.0
    for counter in range(num_vertices):
        angle += 2*pi/num_vertices 
        vertice_x = math.cos(angle)*radius
        vertice_y = math.sin(angle)*radius
        # x = np.float64(round(x, 3))
        # y = np.float64(round(y, 3))
        
        # Para pegar somente o semi circulo inferior, ignore os primeiros 15 pontos
        if counter > 14:
            vertices.append((vertice_x,vertice_y))

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_head(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
    # Funcao para calcular os vertices aqui
    
    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (+0.0, +0.65),
        (+0.3, +0.0),
        (-0.3, +0.0),
        (+0.0, -0.45),
    ]

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_hair(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
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

def create_hair_outline(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
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

def create_ellipse(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, radius=1.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP, eccentricity=1):
    
    num_vertices = 32 # define a "qualidade" do circulo
    pi = 3.14
    counter = 0
    vertices = []
    offset_x = x
    offset_y = y

    angle = 0.0
    for counter in range(num_vertices):
        angle += 2*pi/num_vertices 
        x = math.cos(angle)*radius + offset_x
        y = math.sin(angle)*radius*eccentricity + offset_y
        # x = np.float64(round(x, 3))
        # y = np.float64(round(y, 3))

        vertices.append((x,y))

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_ear(program=None, x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
    num_vertices = 32 # define a "qualidade" do circulo
    pi = 3.14
    counter = 0
    radius = 0.06
    vertices = []

    angle = 0.0
    for counter in range(num_vertices):
        angle += 2*pi/num_vertices 
        vertice_x = math.cos(angle)*radius
        vertice_y = math.sin(angle)*radius
        
        vertices.append((vertice_x,vertice_y))

    return [vertices, x, y, scale, rotation, R, G, B, mode]

def create_ear_line(program=None, side='A', x=0.0, y=0.0, scale=0.0, rotation=0.0, R=0.1, G=0.1, B=0.1, mode=GL_LINE_STRIP):
    
    # Funcao para calcular os vertices aqui
    
    # Preenchendo as coordenadas de cada vértice
    vertices = [
        (+0.033, -0.03),
        (+0.01, -0.035),
        (-0.01, -0.02),
        (+0.00, +0.00),
        (-0.011, +0.019),
        (+0.01, +0.042),
        (+0.032, +0.03),
    ]

    if side == 'B':
        vertices = [
            (-0.033, -0.03),
            (-0.01, -0.035),
            (+0.01, -0.02),
            (-0.00, +0.00),
            (+0.011, +0.019),
            (-0.01, +0.042),
            (-0.032, +0.03),
        ]

    return [vertices, x, y, scale, rotation, R, G, B, mode]