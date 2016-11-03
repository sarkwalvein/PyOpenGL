from OpenGL.GLU import *
from OpenGL.GL import *
import sys
sys.path.append('..')
from pygameSkell import *

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor (1.0, 1.0, 1.0)
    glLoadIdentity ()             #/* clear the matrix */
            #/* viewing transformation  */
    gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glScale (1.0, 2.0, 1.0)      #/* modeling transformation */ 
    glutWireCube (1.0)
    glFlush ()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    glFrustum (-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode (GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__': main()
    
