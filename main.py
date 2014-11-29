from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys




class Graphics(object):

    def __init__(self, name="graphics", window_size=(500, 500)):
        self.name = name
        self.window_size = window_size
        self.initGL()

    def initGL(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(*self.window_size)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(self.name)

        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        lightZeroPosition = [10., 4., 10., 1.]
        lightZeroColor = [0.8, 1.0, 0.8, 1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(40., 1., 1., 40.)
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 10,
                  0, 0, 0,
                  0, 1, 0)
        glPushMatrix()
        glutMainLoop()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        color = [1.0, 0., 0., 1.]
        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
#        glTranslate(2, 0, 0)
#        glutSolidSphere(2, 20, 20)
        glTranslate(2, 0, 0)
        glutSolidCube(3)
        glPopMatrix()
        glutSwapBuffers()

    def drawRectangles(self, rectangles):



if __name__ == '__main__':
    g = Graphics()