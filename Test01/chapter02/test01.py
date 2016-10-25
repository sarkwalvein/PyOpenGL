import sys
sys.path.append('..')

from pygameSkell import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    # Test Drawing Code here ----
    circle_points = 100
    glBegin(GL_LINE_LOOP)
    for i in range(circle_points):
        angle = 2*math.pi*i/circle_points
        glVertex(math.cos(angle), math.sin(angle))

    glEnd()
    # ---------------------------
    glPopMatrix()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    #glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    #glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 1.0)
    #glMatrixMode(GL_MODELVIEW)
    #glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()
    

if __name__ == '__main__': main()
    