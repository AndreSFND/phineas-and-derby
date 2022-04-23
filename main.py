import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

from utils import create_window, create_program, upload_data, draw_object
from objects import create_triangle, create_nose, create_mouth

objects = list()
current_object = 0

def create_objects(program):
    # program, x, y, rotation, R, G, B, render_mode
    objects.append( create_triangle(program, +0.0, +0.0, 0.0, 0.0, 0.0, 1.0, GL_TRIANGLE_FAN) )
    objects.append( create_nose(program, -0.5, +0.0, 0.0, 0.81, 0.49, 0.39, GL_TRIANGLE_STRIP) )
    objects.append( create_mouth(program, -0.5, +0.0, 0.0, 0.39, 0.01, 0.02, GL_TRIANGLE_FAN) )

def move_object(x_offset, y_offset):
    global objects

    objects[current_object][1] += x_offset
    objects[current_object][2] += y_offset

def rotate_object(offset):
    global objects

    objects[current_object][3] += offset

def key_event(window,key,scancode,action,mods):
    global objects, current_object

    # Translates object
    if key == 265: move_object(+0.00, +0.01) #cima
    if key == 264: move_object(+0.00, -0.01) #baixo
    if key == 263: move_object(-0.01, +0.00) #esquerda
    if key == 262: move_object(+0.01, +0.00) #direita
    # Rotates object
    if key == 65:  rotate_object(-2) #esquerda
    if key == 68:  rotate_object(+2) #direita
    # Switch between objects
    if key == 81 and action == 1: current_object = (current_object+1) % len(objects)
    if key == 69 and action == 1: current_object = (current_object-1) % len(objects)

def main():
    window = create_window()
    program = create_program()

    create_objects(program)

    concatenated_vertices = []    
    for obj in objects:
        concatenated_vertices += obj[0]

    vertices = np.zeros(len(concatenated_vertices), [("position", np.float32, 2)])
    vertices["position"] = concatenated_vertices

    upload_data(program, vertices)

    loc_color = glGetUniformLocation(program, "color")
    glfw.set_key_callback(window,key_event)
    glfw.show_window(window)

    while not glfw.window_should_close(window):

        glfw.poll_events() 
        
        # Para debugar, descomente o modo de poligonos:
        # glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
        
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        
        start_index = 0
        for obj in objects:
            draw_object(obj, program, loc_color, start_index)
            start_index += len( obj[0] )

        glfw.swap_buffers(window)

if __name__ == "__main__":
    main()