import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

from utils import create_window, create_program, upload_data, draw_object
from objects import create_ellipse, create_triangle, create_nose, create_mouth, create_head, create_hair, create_hair_outline

objects = list()
current_object = 0

def create_objects(program):
    # program, x, y, scale_x, scale_y, rotation, R, G, B, render_mode

    # Hair
    objects.append( create_hair(program=program, x=-0.4, y=1, scale=0.6, R=0.87, G=0.18, B=0.09, mode=GL_TRIANGLE_FAN ) )
    # Hair outline
    objects.append( create_hair_outline(program=program, x=-0.4, y=1, scale=0.6, R=0.43, G=0.17, B=0.25, mode=GL_LINE_STRIP ) )
    # Head
    objects.append( create_head(program, R=0.98, G=0.72, B=0.60, mode=GL_TRIANGLE_STRIP) )
    # Nose
    objects.append( create_nose(program, x=-0.03, y=+0.05, scale=-0.95, R=0.81, G=0.49, B=0.39, mode=GL_TRIANGLE_STRIP) )
    # Mouth
    objects.append( create_mouth(program, x=+0.00, y=-0.05, scale=-0.75, R=0.39, G=0.01, B=0.02, mode=GL_TRIANGLE_FAN) )
    # objects.append( create_ellipse(program, x=-0.083, y=+0.078, scale=0.0, rotation=0.0, radius=0.07, eccentricity=2, R=0.0, G=0.0, B=0.0, mode=GL_TRIANGLE_FAN) )
    # objects.append( create_ellipse(program, x=+0.017, y=+0.078, rotation=0.0, radius=0.07, eccentricity=2, R=0.0, G=0.0, B=0.0, mode=GL_TRIANGLE_FAN) )
    # objects.append( create_ellipse(program, x=-0.079, y=+0.078, rotation=0.0, radius=0.06, eccentricity=2, R=1.0, G=1.0, B=1.0, mode=GL_TRIANGLE_FAN) )
    # objects.append( create_ellipse(program, x=+0.020, y=+0.078, rotation=0.0, radius=0.06, eccentricity=2, R=1.0, G=1.0, B=1.0, mode=GL_TRIANGLE_FAN) )
    # objects.append( create_ellipse(program, x=-0.076, y=+0.078, rotation=0.0, radius=0.05, eccentricity=1.3, R=0.094, G=0.109, B=0.388, mode=GL_TRIANGLE_FAN) )
    # objects.append( create_ellipse(program, x=+0.023, y=+0.078, rotation=0.0, radius=0.05, eccentricity=1.3, R=0.094, G=0.109, B=0.388, mode=GL_TRIANGLE_FAN) )

def move_object(x_offset, y_offset):
    global objects

    objects[current_object][1] += x_offset
    objects[current_object][2] += y_offset

def scale_object(scale):
    global objects

    objects[current_object][3] += scale

def rotate_object(offset):
    global objects

    objects[current_object][4] += offset

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
    # Scales object
    if key == 334:  scale_object(+0.01) #zoom in
    if key == 333:  scale_object(-0.01) #zoom out
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
