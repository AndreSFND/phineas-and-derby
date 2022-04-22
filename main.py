import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

glfw.init()
glfw.window_hint(glfw.VISIBLE, glfw.FALSE);
window = glfw.create_window(720, 600, "Cores", None, None)
glfw.make_context_current(window)

vertex_code = """
        attribute vec2 position;
        uniform mat4 mat_transformation;
        void main(){
            gl_Position = mat_transformation * vec4(position,0.0,1.0);
        }
        """

fragment_code = """
        uniform vec4 color;
        void main(){
            gl_FragColor = color;
        }
        """

# Request a program and shader slots from GPU
program  = glCreateProgram()
vertex   = glCreateShader(GL_VERTEX_SHADER)
fragment = glCreateShader(GL_FRAGMENT_SHADER)

# Set shaders source
glShaderSource(vertex, vertex_code)
glShaderSource(fragment, fragment_code)

# Compile shaders
glCompileShader(vertex)
if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(vertex).decode()
    print(error)
    raise RuntimeError("Erro de compilacao do Vertex Shader")

glCompileShader(fragment)
if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(fragment).decode()
    print(error)
    raise RuntimeError("Erro de compilacao do Fragment Shader")

# Attach shader objects to the program
glAttachShader(program, vertex)
glAttachShader(program, fragment)

# Build program
glLinkProgram(program)
if not glGetProgramiv(program, GL_LINK_STATUS):
    print(glGetProgramInfoLog(program))
    raise RuntimeError('Linking error')
    
# Make program the default program
glUseProgram(program)

# preparando espaço para 3 vértices usando 2 coordenadas (x,y)
vertices = np.zeros(3, [("position", np.float32, 2)])

# preenchendo as coordenadas de cada vértice
vertices['position'] = [
                            ( -0.5, -0.4), # vertice 0
                            (-0.6, -0.6), # vertice 1
                            (-0.4, -0.6) # vertice 2
                        ]

# Request a buffer slot from GPU
buffer = glGenBuffers(1)
# Make this buffer the default one
glBindBuffer(GL_ARRAY_BUFFER, buffer)

# Upload data
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
glBindBuffer(GL_ARRAY_BUFFER, buffer)

# Bind the position attribute
# --------------------------------------
stride = vertices.strides[0]
offset = ctypes.c_void_p(0)

loc = glGetAttribLocation(program, "position")
glEnableVertexAttribArray(loc)

glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)

loc_color = glGetUniformLocation(program, "color")
R = 1.0
G = 0.0
B = 0.0

# exemplo para matriz de translacao
t_x = 0
t_y = 0

def key_event(window,key,scancode,action,mods):
    global t_x, t_y
    
#     print('[key event] key=',key)
#     print('[key event] scancode=',scancode)
#     print('[key event] action=',action)
#     print('[key event] mods=',mods)
#     print('-------')
    if key == 265: t_y += 0.01 #cima
    if key == 264: t_y -= 0.01 #baixo
    if key == 263: t_x -= 0.01 #esquerda
    if key == 262: t_x += 0.01 #direita
    
glfw.set_key_callback(window,key_event)

glfw.show_window(window)

t_y = 1
t_x = 1
while not glfw.window_should_close(window):

    glfw.poll_events() 

    
    glClear(GL_COLOR_BUFFER_BIT) 
    glClearColor(1.0, 1.0, 1.0, 1.0)
    
    
    #Draw Triangle
    mat_translation = np.array([    1.0, 0.0, 0.0, t_x, 
                                    0.0, 1.0, 0.0, t_y, 
                                    0.0, 0.0, 1.0, 0.0, 
                                    0.0, 0.0, 0.0, 1.0], np.float32)
    
    loc = glGetUniformLocation(program, "mat_transformation")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_translation)

    
    glDrawArrays(GL_TRIANGLES, 0, len(vertices))
    glUniform4f(loc_color, R, G, B, 1.0) ### modificando a cor do objeto!

    glfw.swap_buffers(window)

# glfw.terminate()