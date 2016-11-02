# Based on example 2-10 http://www.glprogramming.com/red/chapter02.html
# Also read:
# http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/tests/gldrawelements_string.py
# http://pyopengl.sourceforge.net/context/
# http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/tests/shader_3.py

from OpenGL.GLU import *
from OpenGL.GL import *
import numpy
import sys
sys.path.append('..')
from pygameSkell import *

vertices = numpy.array( [
                        [25, 25],
                        [100, 325],
                        [175, 25],
                        [175, 325],
                        [250, 25],
                        [325, 325] ] , 'i' )
colors = numpy.array( [
                      [1.0, 0.2, 0.2],
                      [0.2, 0.2, 1.0],
                      [0.8, 1.0, 0.2],
                      [0.75, 0.75, 0.75],
                      [0.35, 0.35, 0.35],
                      [0.5, 0.5, 0.5] ] , 'f')

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
    glEnableClientState (GL_COLOR_ARRAY)
    glEnableClientState (GL_VERTEX_ARRAY)
    glColorPointer (3, GL_FLOAT, 0, colors.tostring() )
    glVertexPointer (2, GL_INT, 0, vertices.tostring() )

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    # Test Drawing Code here ----
    glBegin(GL_TRIANGLES)
    glArrayElement (2)
    glArrayElement (3)
    glArrayElement (5)
    glEnd()
    # ---------------------------
    glPopMatrix()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluOrtho2D (0.0, w, 0.0, h)

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
    