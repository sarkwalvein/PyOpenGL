#http://www.glprogramming.com/red/chapter02.html
#Example 2-7 : Marking Polygon Boundary Edges


from OpenGL.GLU import *
from OpenGL.GL import *
import sys
sys.path.append('..')
from pygameSkell import *

def drawOneLine(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glEnd()
    
def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    glClear (GL_COLOR_BUFFER_BIT)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_POLYGON)
    glEdgeFlag(GL_TRUE)
    glVertex(50,50)
    glEdgeFlag(GL_FALSE)
    glVertex(300,100)
    glEdgeFlag(GL_TRUE)
    glVertex(200,200)
    glEnd()
    glFlush ()
    
    
    #glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0.0, w, 0.0, h);
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 300)
    glutInitWindowPosition (100, 100)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__': main()
