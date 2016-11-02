# Based on example 2-11 http://www.glprogramming.com/red/chapter02.html

from OpenGL.GLU import *
from OpenGL.GL import *
import numpy
import sys
sys.path.append('..')
from pygameSkell import *

vertices = numpy.array( [
                        [0, 0, 0],
                        [100, 0, 0],
                        [100, 100, 0],
                        [0, 100, 0],
                        [0, 0, 100],
                        [100, 0, 100],
                        [100, 100, 100],
                        [0, 100, 100],
                        ] , 'i' )
colors = numpy.array( [
                      [1, 1, 1],
                      [1, 1, 0],
                      [1, 0, 0],
                      [0, 1, 0],
                      [0, 1, 1],
                      [0, 0, 1],
                      [1, 0, 1],
                      [0, 0, 0],
                      ] , 'f')

allIndices = numpy.array( [
                          [4, 5, 6, 7, 1, 2, 6, 5, 
                           0, 1, 5, 4, 0, 3, 2, 1, 
                           0, 4, 7, 3, 2, 3, 7, 6]
                           ], 'i' )
                            
def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
    glEnableClientState (GL_COLOR_ARRAY)
    glEnableClientState (GL_VERTEX_ARRAY)
    glColorPointer (3, GL_FLOAT, 0, colors.tostring() )
    glVertexPointer (3, GL_INT, 0, vertices.tostring() )

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    # Test Drawing Code here ----
    # glBegin(GL_TRIANGLES)
    # glArrayElement (2)
    # glArrayElement (3)
    # glArrayElement (5)
    # glEnd()
    glDrawElements(GL_QUADS, allIndices.size, GL_UNSIGNED_INT, allIndices.tostring())
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
    