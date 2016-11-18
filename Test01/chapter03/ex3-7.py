# Based on example 3-6 http://www.glprogramming.com/red/chapter03.html

from OpenGL.GLU import *
from OpenGL.GL import *
import sys
sys.path.append('..')
from pygameSkell import *

shoulder = 0; elbow = 0;

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def drawFinger(ang0, ang1):
    glRotatef (ang0, 0.0, 0.0, 1.0)
    glTranslatef (1.0, 0.0, 0.0)
    glPushMatrix()
    glScalef (2.0, 0.4, 1.0)
    glutWireCube (1.0)
    glPopMatrix()

    glTranslatef (1.0, 0.0, 0.0)
    glRotatef (ang1, 0.0, 0.0, 1.0)
    glTranslatef (1.0, 0.0, 0.0)
    glPushMatrix()
    glScalef (2.0, 0.4, 1.0)
    glutWireCube (1.0)
    glPopMatrix()
    
    glTranslatef (1.0, 0.0, 0.0)
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    # Test Drawing Code here ----
    glScale(.5,.5,.5)
    glTranslatef (-1.0, 0.0, 0.0)
    drawFinger(shoulder, elbow)
    glTranslatef (0.0, 0.2-0.2*0.2, 0.0)
    glScale(.2, .2, .2)
    glPushMatrix()
    glTranslatef (0.0, 0.0, -2.5)
    drawFinger(0, elbow)
    glPopMatrix()
    glPushMatrix()
    glTranslatef (0.0, 0.0, -2.5+5/3)
    drawFinger(0, elbow)
    glPopMatrix()
    glPushMatrix()
    glTranslatef (0.0, 0.0, -2.5+10/3)
    drawFinger(0, elbow)
    glPopMatrix()
    glPushMatrix()
    glTranslatef (0.0, 0.0, 2.5)
    drawFinger(0, elbow)
    glPopMatrix()
    glPushMatrix()
    glTranslatef (0.0, -.2*2/.2+.2*2, -2.5)
    drawFinger(0, -elbow)
    glPopMatrix()
    # ---------------------------
    glPopMatrix()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(65.0, w/h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef (0.0, 0.0, -5.0)

def keyboard (key, x, y):
    global shoulder, elbow
    if key == 's':
        shoulder = (shoulder + 5) % 360
    elif key == 'w':
        shoulder = (shoulder - 5) % 360
    elif key == 'e':
        elbow = (elbow + 5) % 360
    elif key == 'd':
        elbow = (elbow - 5) % 360

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
 
if __name__ == '__main__': main()
