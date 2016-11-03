from OpenGL.GLU import *
from OpenGL.GL import *
import sys
sys.path.append('..')
from pygameSkell import *

px = 0
py = 0
pz = 0

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor (1.0, 1.0, 1.0)
    glLoadIdentity ()             #/* clear the matrix */
            #/* viewing transformation  */
    #gluLookAt( cameraPosition (3f), whereToAimTheCamera (3f), whichWayIsUp (3f) )
    gluLookAt (0.0, 0.0, 5.0, px, py, pz, 0.0, 1.0, 0.0)
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
    
