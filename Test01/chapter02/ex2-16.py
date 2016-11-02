# Based on example 2-16 http://www.glprogramming.com/red/chapter02.html

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
                            
import math
def normalize(v):
    d = math.sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]) 
    if d == 0.0:
        raise ArithmeticError("zero length vector")    

    v[0] /= d
    v[1] /= d
    v[2] /= d 

def normcrossprod(v1, v2, out): 
    out[0] = v1[1]*v2[2] - v1[2]*v2[1]
    out[1] = v1[2]*v2[0] - v1[0]*v2[2]
    out[2] = v1[0]*v2[1] - v1[1]*v2[0]
    normalize(out)

def subdivide(v1, v2, v3): 
    v12 = numpy.empty(3, 'f')
    v23 = numpy.empty(3, 'f')
    v31 = numpy.empty(3, 'f')
    
    for i in range(3):
        v12[i] = v1[i]+v2[i]
        v23[i] = v2[i]+v3[i]    
        v31[i] = v3[i]+v1[i]   

    normalize(v12)
    normalize(v23)
    normalize(v31)
    drawtriangle(v1, v12, v31)
    drawtriangle(v2, v23, v12)
    drawtriangle(v3, v31, v23)
    drawtriangle(v12, v23, v31)

def drawtriangle(v1, v2, v3): 
    glBegin(GL_TRIANGLES) 
    glNormal3fv(v1)
    glVertex3fv(v1)    
    glNormal3fv(v2)
    glVertex3fv(v2)
    glNormal3fv(v3)
    glVertex3fv(v3)
    glEnd()

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    # Test Drawing Code here ----

    for i in range(20):
        subdivide(vdata[tindices[i][0]],       
                  vdata[tindices[i][1]],       
                  vdata[tindices[i][2]])


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
    