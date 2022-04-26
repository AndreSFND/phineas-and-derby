import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

def create_window():
    # Inicializando janela
    glfw.init()
    # Definindo parametros da janela
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    # Cria a janela
    window = glfw.create_window(720, 600, "Phineas and Derby", None, None)
    # Define a janela como a principal
    glfw.make_context_current(window)

    return window

def create_program():
    # GLSL para Vertex Shader
    vertex_code = """
            attribute vec2 position;
            uniform mat4 mat_transformation;
            void main(){
                gl_Position = mat_transformation * vec4(position,0.0,1.0);
            }
            """

    # GLSL para Fragment Shader
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

    # Compile vertex shader
    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Vertex Shader")

    # Compile fragment shader
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

    return program

def upload_data(program, vertices):
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

def multiplica_matriz(a,b):
    m_a = a.reshape(4,4)
    m_b = b.reshape(4,4)
    m_c = np.dot(m_a,m_b)
    c = m_c.reshape(1,16)
    return c

def draw_object(obj, program, loc_color, start_index):

    rad = math.radians(obj[5]) 
    c = math.cos(rad)
    s = math.sin(rad)

    # Definindo a matriz de translacao
    mat_translation = np.array([    1.0, 0.0, 0.0, obj[1],
                                    0.0, 1.0, 0.0, obj[2],
                                    0.0, 0.0, 1.0, 0.0,
                                    0.0, 0.0, 0.0, 1.0,], np.float32)

    # Definindo a matriz de escala
    mat_scale       = np.array([    obj[3], 0.0, 0.0, 0.0,
                                    0.0, obj[4], 0.0, 0.0,
                                    0.0, 0.0, 1.0, 0.0,
                                    0.0, 0.0, 0.0, 1.0,], np.float32)

     # Definindo a matriz de rotacao
    mat_rotation    = np.array([    c,   -s,  0.0, 0.0,
                                    s,   c,   0.0, 0.0,
                                    0.0, 0.0, 1.0, 0.0,
                                    0.0, 0.0, 0.0, 1.0,], np.float32)
    
    mat_transformation = multiplica_matriz(mat_translation,mat_scale)
    mat_transformation = multiplica_matriz(mat_rotation,mat_transformation)

    loc = glGetUniformLocation(program, "mat_transformation")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transformation)
    
    # Modificando a cor do objeto
    glUniform4f(loc_color, obj[6], obj[7], obj[8], 1.0)

    # Desenhando arestas
    glDrawArrays(obj[9], start_index, len(obj[0]))