from OpenGL.GLU import *
from OpenGL.GL import *
import sys
sys.path.append('..')
from pygameSkell import *

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_SMOOTH)

def triangle():
    glBegin (GL_TRIANGLES)
    glColor3f (1.0, 0.0, 0.0)
    glVertex2f (5.0, 5.0)
    glColor3f (0.0, 1.0, 0.0)
    glVertex2f (25.0, 5.0)
    glColor3f (0.0, 0.0, 1.0)
    glVertex2f (5.0, 25.0)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Test Drawing Code here ----
    triangle ()
    glFlush ()
    # ---------------------------
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    if w <= h:
        gluOrtho2D (0.0, 30.0, 0.0, 30.0*h/w)
    else:
        gluOrtho2D (0.0, 30.0*w/h, 0.0, 30.0)

    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__': main()
