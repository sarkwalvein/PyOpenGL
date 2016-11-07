from OpenGL.GLU import *
from OpenGL.GL import *
import numpy
import time
import sys
sys.path.append('..')
from pygameSkell import *

px = 0; py = 5; pz = 0
ux = 0; uy = 0; uz = 1
radius = 5
theta = 0
phi = 0
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
        self._lastIii = -1
        
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
        self._insertVertex(v3)
        self._insertVertex(v2)
        
    def _insertVertex(self, v):
        idx = self._vertexMap.get(v.tobytes())
        if idx == None:
            idx = len(self._vertexList)
            self._vertexList.append(v)
            self._vertexMap[v.tobytes()]=idx
        self._vertexIndices.append(idx)
        
    def setPointers(self):
        # glEnableClientState (GL_COLOR_ARRAY)
        glEnableClientState (GL_VERTEX_ARRAY)
        glColorPointer (3, GL_FLOAT, 0, self._colorArray )
        glVertexPointer (3, GL_FLOAT, 0, self._vertexArray )
        
    def draw(self, iii = 0):
        if self._lastIii != iii:
            self._prepareColors(iii)
            self._lastIii = iii
            
        glDrawElements(GL_TRIANGLES, self._vertexIndices.size, GL_UNSIGNED_INT, self._vertexIndices)
        
    def _prepareColors(self, iii):
        for i in range(len(self._colorArray)):
            self._colorArray[i][0]=.5 #(iii%4+1)/4
            self._colorArray[i][1]=.5 #((iii//4)%4+1)/4
            self._colorArray[i][2]=.5 #((iii//16)%4+1)/4
            iii+=1
        
ball = MyBall(3)


def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
    glCullFace(GL_BACK)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)  #less or equal
    glClearDepth(1.0)
    ball.setPointers()

def display():
    bodyRadius = 8/4
    wingRadius = 9/4
    wingPosition = -.2
    enginePosRatio = .5
    engineRadius = 1/4
    engineLength = 2/4
    tailRadius = 3/4
    widthBase = 1/8
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity ()             #/* clear the matrix */
            #/* viewing transformation  */
    #gluLookAt( cameraPosition (3f), whereToAimTheCamera (3f), whichWayIsUp (3f) )
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, ux, uy, uz)
    
    # Main
    glColor (0,.2,0)    
    glScale (bodyRadius, 2.0*widthBase, 2.0*widthBase)      #/* modeling transformation */ 
    ball.draw()
    # Wing
    glColor (1,1, .6)    
    glLoadIdentity ()
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, ux, uy, uz)
    glTranslate(wingPosition*bodyRadius,0,0)
    glScale (widthBase*2, wingRadius, 0.5*widthBase)      #/* modeling transformation */ 
    ball.draw()
    # -- Engines
    glLoadIdentity ()
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, ux, uy, uz)
    glTranslate(wingPosition*bodyRadius, enginePosRatio*wingRadius ,0)
    glRotate ((20*i_init)%360, 1, 0, 0)
    glScale (engineLength, engineRadius, engineRadius)      
    glColor (.5, .5, 0)    
    ball.draw()
    glTranslate(-2*engineLength,0,0)
    glScale (1/10, 1/10, 1.5)
    glColor (1,1, .6)    
    ball.draw()
    
    glLoadIdentity ()
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, ux, uy, uz)
    glTranslate(wingPosition*bodyRadius, -enginePosRatio*wingRadius ,0)
    glRotate ((20*i_init)%360, 1, 0, 0)
    glScale (engineLength, engineRadius, engineRadius)      
    glColor (.5, .5, 0)    
    ball.draw()
    glTranslate(-2*engineLength,0,0)
    glScale (1/10, 1/10, 1.5)
    glColor (1,1, .6)    
    ball.draw()
    
    # Tail
    glLoadIdentity ()
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, ux, uy, uz)
    glTranslate(bodyRadius,0,0)
    glScale (0.5*widthBase, tailRadius, widthBase)
    glColor (1,1, .6)    
    ball.draw()
    # -- Stabilizer
    glColor (1,1, 0)    
    glLoadIdentity ()
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, ux, uy, uz)
    glTranslate(bodyRadius,tailRadius,0)
    glScale (widthBase, widthBase/2, widthBase/2)
    ball.draw()
    glLoadIdentity ()
    gluLookAt (px, py, pz, 0.0, 0.0, 0.0, ux, uy, uz)
    glTranslate(bodyRadius,-tailRadius,0)
    glScale (widthBase, widthBase/2, widthBase/2)
    ball.draw()
    
    #glutWireCube (1.0)
    glFlush ()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    glFrustum (-1.0, 1.0, -1.0, 1.0, 1.5, 120.0)
    glMatrixMode (GL_MODELVIEW)

def angnor(ang):
    while ang > math.pi:
        ang-=2*math.pi
    while ang < -math.pi:
        ang+=2*math.pi
    return ang
    
def calcCamera():
    global px, py, pz
    global ux, uy, uz
    vxy = radius * math.sin(theta)
    px = vxy * math.cos(phi)
    py = vxy * math.sin(phi)
    pz = radius * math.cos(theta)
    
    vxy = radius * math.sin(theta+.1)
    ux = vxy * math.cos(phi)
    uy = vxy * math.sin(phi)
    uz = radius * math.cos(theta+.1)
    
def keyFun(chr, x, y):
    global radius, phi, theta
    
    #if -math.pi/2 < theta < math.pi/2:
    phinc = .1
    #else:
    #    phinc = -.1
    if chr == 'w':
        theta=angnor(theta-.1)
    if chr == 'a':
        phi=angnor(phi-phinc)
    if chr == 's':
        theta=angnor(theta+.1)
    if chr == 'd':
        phi=angnor(phi+phinc)
    if chr == 'q':
        radius-=.1
    if chr == 'e':
        radius+=.1
        
    if radius<0:
        radius = 0
        
    calcCamera()
    

def idle():
    global i_init
    time.sleep(1/60)
    i_init += 1
    
        
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    #glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyFun)
    glutIdleFunc(idle)
    calcCamera()
    glutMainLoop()

if __name__ == '__main__': main()
    
