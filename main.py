import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

from utils import create_window, create_program, draw_object
from objects import create_triangle

objects = list()
current_object = 0

def move_object(x_offset, y_offset):
    global objects

    objects[current_object][1] += x_offset
    objects[current_object][2] += y_offset

def key_event(window,key,scancode,action,mods):    
    if key == 265: move_object(+0.00, +0.01) #cima
    if key == 264: move_object(+0.00, -0.01) #baixo
    if key == 263: move_object(-0.01, +0.00) #esquerda
    if key == 262: move_object(+0.01, +0.00) #direita

def main():
    window = create_window()
    program = create_program()

    objects.append( create_triangle(program) ) # Creates a triangle

    loc_color = glGetUniformLocation(program, "color")
    glfw.set_key_callback(window,key_event)
    glfw.show_window(window)

    while not glfw.window_should_close(window):

        glfw.poll_events() 
        
        glClear(GL_COLOR_BUFFER_BIT) 
        glClearColor(1.0, 1.0, 1.0, 1.0)
        
        for obj in objects:
            draw_object(obj, program, loc_color)

        glfw.swap_buffers(window)

if __name__ == "__main__":
    main()