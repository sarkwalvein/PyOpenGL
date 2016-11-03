from OpenGL.GLU import *
from OpenGL.GL import *
import numpy
import time
import sys
sys.path.append('..')
from pygameSkell import *

px = 0
py = 0
pz = 0
anx = 0
i_init = 0
                           
import math
class MyBall:
    def __init__(self, subdiv = 4):
        self._subdiv = subdiv
        X = .525731112119133606 
        Z = .850650808352039932
        self._vdata = numpy.array ( [    
                [-X, 0.0, Z], [X, 0.0, Z], [-X, 0.0, -Z], [X, 0.0, -Z],    
                [0.0, Z, X], [0.0, Z, -X], [0.0, -Z, X], [0.0, -Z, -X],    
                [Z, X, 0.0], [-Z, X, 0.0], [Z, -X, 0.0], [-Z, -X, 0.0] 
                ], 'f' )
        self._tindices = [ 
                [0,4,1], [0,9,4], [9,5,4], [4,5,8], [4,8,1],    
                [8,10,1], [8,3,10], [5,3,8], [5,2,3], [2,7,3],    
                [7,10,3], [7,6,10], [7,11,6], [11,0,6], [0,1,6], 
                [6,1,10], [9,0,11], [9,11,2], [9,2,5], [7,2,11] 
                ]
        self._vertexList = []
        self._vertexMap = {}
        self._vertexIndices = []
        self._generateBall()
        
    def _generateBall(self):
        for i in range(20):
            self._subdivide(self._vdata[self._tindices[i][0]],       
                            self._vdata[self._tindices[i][1]],       
                            self._vdata[self._tindices[i][2]], self._subdiv)

        # Additional processing
        self._vertexArray = numpy.array(self._vertexList, 'f')
        self._vertexIndices = numpy.array(self._vertexIndices, 'i')
        self._vertexList = []
        self._vertexMap = {}
        self._colorArray = numpy.empty(self._vertexArray.shape,'f')
        
    def _normalize(self, v):
        d = math.sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]) 
        if d == 0.0:
            raise ArithmeticError("zero length vector")    
    
        v[0] /= d
        v[1] /= d
        v[2] /= d 

    def _normcrossprod(self, v1, v2, out): 
        out[0] = v1[1]*v2[2] - v1[2]*v2[1]
        out[1] = v1[2]*v2[0] - v1[0]*v2[2]
        out[2] = v1[0]*v2[1] - v1[1]*v2[0]
        self._normalize(out)

    def _subdivide(self, v1, v2, v3, depth): 
        v12 = numpy.empty(3, 'f')
        v23 = numpy.empty(3, 'f')
        v31 = numpy.empty(3, 'f')
    
        if depth == 0:
            self._drawtriangle(v1, v2, v3);
            return
    
        for i in range(3):
            v12[i] = v1[i]+v2[i]
            v23[i] = v2[i]+v3[i]    
            v31[i] = v3[i]+v1[i]   
    
        self._normalize(v12)
        self._normalize(v23)
        self._normalize(v31)
        self._subdivide(v1, v12, v31, depth-1)
        self._subdivide(v2, v23, v12, depth-1)
        self._subdivide(v3, v31, v23, depth-1)
        self._subdivide(v12, v23, v31, depth-1)

    def _drawtriangle(self, v1, v2, v3): 
        self._insertVertex(v1)
        self._insertVertex(v2)
        self._insertVertex(v3)
        
    def _insertVertex(self, v):
        idx = self._vertexMap.get(v.tobytes())
        if idx == None:
            idx = len(self._vertexList)
            self._vertexList.append(v)
            self._vertexMap[v.tobytes()]=idx
        self._vertexIndices.append(idx)
        
    def setPointers(self):
        glEnableClientState (GL_COLOR_ARRAY)
        glEnableClientState (GL_VERTEX_ARRAY)
        glColorPointer (3, GL_FLOAT, 0, self._colorArray )
        glVertexPointer (3, GL_FLOAT, 0, self._vertexArray )
        
    def draw(self, iii = 0):
        self._prepareColors(iii)
        glDrawElements(GL_TRIANGLES, self._vertexIndices.size, GL_UNSIGNED_INT, self._vertexIndices)
        
    def _prepareColors(self, iii):
        for i in range(len(self._colorArray)):
            self._colorArray[i][0]=(iii%4+1)/4
            self._colorArray[i][1]=((iii//4)%4+1)/4
            self._colorArray[i][2]=((iii//16)%4+1)/4
            iii+=1
        
ball = MyBall(3)


def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor (1.0, 1.0, 1.0)
    glLoadIdentity ()             #/* clear the matrix */
            #/* viewing transformation  */
    #gluLookAt( cameraPosition (3f), whereToAimTheCamera (3f), whichWayIsUp (3f) )
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
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

def keyFun(chr, x, y):
    global px
    global py
    global pz
    if chr == 'w':
        py+=.1
    if chr == 'a':
        px-=.1
    if chr == 's':
        py-=.1
    if chr == 'd':
        px+=.1
        
def main():
    glutInit(sys.argv)
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyFun)
    glutMainLoop()

if __name__ == '__main__': main()
    
