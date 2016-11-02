# Based on example 2-13 http://www.glprogramming.com/red/chapter02.html

from OpenGL.GLU import *
from OpenGL.GL import *
import numpy
import sys
sys.path.append('..')
from pygameSkell import *

X = .525731112119133606 
Z = .850650808352039932

vdata = numpy.array ( [    
        [-X, 0.0, Z], [X, 0.0, Z], [-X, 0.0, -Z], [X, 0.0, -Z],    
        [0.0, Z, X], [0.0, Z, -X], [0.0, -Z, X], [0.0, -Z, -X],    
        [Z, X, 0.0], [-Z, X, 0.0], [Z, -X, 0.0], [-Z, -X, 0.0] 
        ], 'f' )

tindices = [ 
           [0,4,1], [0,9,4], [9,5,4], [4,5,8], [4,8,1],    
           [8,10,1], [8,3,10], [5,3,8], [5,2,3], [2,7,3],    
           [7,10,3], [7,6,10], [7,11,6], [11,0,6], [0,1,6], 
           [6,1,10], [9,0,11], [9,11,2], [9,2,5], [7,2,11] 
           ]
                            
def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    # Test Drawing Code here ----
    glBegin(GL_TRIANGLES);    
    for i in range(20):    
        #/* color information here */ 
        glColor(i%2, (i/2)%2, (i/4)%2)
        glVertex3fv(vdata[tindices[i][0]])
        glVertex3fv(vdata[tindices[i][1]])
        glVertex3fv(vdata[tindices[i][2]])
    glEnd()
    # ---------------------------
    glPopMatrix()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluOrtho2D (-1.0, 1, -1.0, 1)

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
    