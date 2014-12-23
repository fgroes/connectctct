import sys
import time
import ctypes
import numpy as np
import OpenGL.GL as gl
import OpenGL.GLUT as glut


class Geometry(object):

    def __init__(self, vertices, colors):
        self.vertices = np.array(vertices)
        self.colors = np.array(colors)

    def __len__(self):
        return self.vertices.shape[0]

    def translate(self, translation=[0, 0]):
        t = np.tile(np.array(translation), [self.vertices.shape[0], 1])
        self.vertices = self.vertices + t


class Rectangle(Geometry):

    def __init__(self, vertices, colors):
        idxs = [0, 1, 2, 1, 3, 2]
        self.vertices = np.array([vertices[i] for i in idxs])
        self.colors = np.array([colors[i] for i in idxs])


class Graphics(object):

    def __init__(self, geos, vertex_code, fragment_code):
        from textures import load_image_uint8
        tex_img = np.zeros(32 * 32, (np.uint8, 4))
        img = load_image_uint8("char2.png")
        tex_img = img
        tex_id = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, tex_id)
        gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
        gl.glTexImage2D(GL_TEXTURE_2D, 0, 3, 32, 32, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, tex_img)

        self.x_pos = 0
        self.y_pos = 0
        self.time = time.time()
        num_vertices = np.sum([len(g) for g in geos])
        data = np.zeros(num_vertices, [("position", np.float32, 3),
                            ("color",    np.float32, 4)])
        cs = []
        vs = []
        for g in geos:
            for c in g.colors:
                cs.append(c)
            for v in g.vertices:
                vs.append(v)
        data["color"] = cs
        data["position"] = vs
        data["position"] = 0.5 * data["position"]
        self.data = data
        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
        glut.glutCreateWindow("Hello world!")
        glut.glutReshapeWindow(512,512)
        glut.glutReshapeFunc(self.reshape)
        glut.glutDisplayFunc(self.display)
        glut.glutIdleFunc(self.idle)
        glut.glutKeyboardFunc(self.keyboard)
        glut.glutMouseFunc(self.mouse)

        program  = gl.glCreateProgram()
        vertex   = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        fragment = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(vertex, vertex_code)
        gl.glShaderSource(fragment, fragment_code)
        gl.glCompileShader(vertex)
        gl.glCompileShader(fragment)
        gl.glAttachShader(program, vertex)
        gl.glAttachShader(program, fragment)
        gl.glLinkProgram(program)
        gl.glDetachShader(program, vertex)
        gl.glDetachShader(program, fragment)
        gl.glUseProgram(program)
        self.buffer = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.buffer)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.data.nbytes, self.data, gl.GL_DYNAMIC_DRAW)
        stride = self.data.strides[0]
        offset = ctypes.c_void_p(0)
        loc = gl.glGetAttribLocation(program, "position")
        gl.glEnableVertexAttribArray(loc)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.buffer)
        gl.glVertexAttribPointer(loc, 3, gl.GL_FLOAT, False, stride, offset)

        offset = ctypes.c_void_p(self.data.dtype["position"].itemsize)
        loc = gl.glGetAttribLocation(program, "color")
        gl.glEnableVertexAttribArray(loc)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.buffer)
        gl.glVertexAttribPointer(loc, 4, gl.GL_FLOAT, False, stride, offset)
        loc = gl.glGetUniformLocation(program, "scale")
        gl.glUniform1f(loc, 1.0)

    def start(self):
        glut.glutMainLoop()

    def idle(self):
        v = 0.005
        self.data["position"][0, 0] += (time.time() - self.time) * v
        self.data["position"][1, 0] += (time.time() - self.time) * v
        self.data["position"][2, 0] += (time.time() - self.time) * v
        if (np.any(self.data["position"][:, 0] > 2)):
            self.data["position"][0, 0] -=4
            self.data["position"][1, 0] -=4
            self.data["position"][2, 0] -=4
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.data.nbytes, self.data, gl.GL_DYNAMIC_DRAW)
#        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.buffer)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, len(self.data))
        glut.glutSwapBuffers()

    def display(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, len(self.data))
        glut.glutSwapBuffers()

    def reshape(self, width, height):
        self.vp_width = width
        self.vp_height = height
        gl.glViewport(self.x_pos, self.y_pos, width, height)

    def keyboard(self, key, x, y ):
        print(key, x, y)
        dp = 10
        if key == "w":
            self.y_pos -= dp
        elif key == "s":
            self.y_pos += dp
        elif key == "a":
            self.x_pos += dp
        elif key == "d":
            self.x_pos -= dp
        gl.glViewport(self.x_pos, self.y_pos, self.vp_width, self.vp_height)

    def mouse(self, button, state, x, y):
        print(button, state, x, y)