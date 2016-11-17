# Based on example 3-6 http://www.glprogramming.com/red/chapter03.html

from OpenGL.GLU import *
from OpenGL.GL import *
import sys
sys.path.append('..')
from pygameSkell import *

year = 0; day = 0;
hour = 0

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    glPushMatrix()
    # Test Drawing Code here ----
    glutWireSphere(1.0, 20, 16)#;   /* draw sun */
    glRotatef (year, 0.0, 1.0, 0.0)
    glTranslatef (2.0, 0.0, 0.0)
    glRotatef (day%360, 0.0, 1.0, 0.0)
    glutWireSphere(0.2, 10, 8)#;    /* draw smaller planet */
    # ---------------------------
    glPopMatrix()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(60.0, w/h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def keyboard (key, x, y):
    global day, year, hour
    if key == 'd':
        day = (day + 10) % 360
    elif key == 'f':
        day = (day - 10) % 360
    elif key == 'y':
        year = (year + 5) % 360
    elif key == 'h':
        year = (year - 5) % 360
    elif key == 'q':
        hour = (hour + 1) % 8760
        day = (hour%24)/24*360
        year = (hour/24/365)*360

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

