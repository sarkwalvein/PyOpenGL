# Based on example 3-5 http://www.glprogramming.com/red/chapter03.html

from OpenGL.GLU import *
from OpenGL.GL import *
import numpy
import sys
sys.path.append('..')
from pygameSkell import *

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    # Test Drawing Code here ----
    eqn = numpy.array ( [ 0.0, 1.0, 0.0, 0.0 ], 'f')
    eqn2 = numpy.array ( [1.0, 0.0, 0.0, 0.0 ], 'f')

    glClear(GL_COLOR_BUFFER_BIT)
    glColor (1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef (0.0, 0.0, -5.0)

#/*    clip lower half -- y < 0          */
    glClipPlane (GL_CLIP_PLANE0, eqn)
    glEnable (GL_CLIP_PLANE0)
#/*    clip left half -- x < 0           */
    glClipPlane (GL_CLIP_PLANE1, eqn2)
    glEnable (GL_CLIP_PLANE1)

    glRotatef (90.0, 1.0, 0.0, 0.0)
    glutWireSphere(1.0, 20, 16)
    #glutSolidSphere(1.0, 20, 16)
    # ---------------------------
    glPopMatrix()
    glFlush()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(60.0,  w/h, 1.0, 20.0)
    glMatrixMode (GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB )
    glutInitWindowSize(500,500)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__': main()


