#http://www.glprogramming.com/red/chapter02.html
#Example 2-5 : Line Stipple Patterns: lines.c

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
    # /* select white for all lines  */
    glColor (1.0, 1.0, 1.0)
    
    # /* in 1st row, 3 lines, each with a different stipple  */
    glEnable (GL_LINE_STIPPLE)
    
    glLineStipple (1, 0x0101)  #/*  dotted  */
    drawOneLine (50.0, 125.0, 150.0, 125.0)
    glLineStipple (1, 0x00FF)  #/*  dashed  */
    drawOneLine (150.0, 125.0, 250.0, 125.0)
    glLineStipple (1, 0x1C47)  #/*  dash/dot/dash  */
    drawOneLine (250.0, 125.0, 350.0, 125.0)
    # /* in 2nd row, 3 wide lines, each with different stipple */
    glLineWidth (5.0)
    glLineStipple (1, 0x0101) # /*  dotted  */
    drawOneLine (50.0, 100.0, 150.0, 100.0)
    glLineStipple (1, 0x00FF)  #/*  dashed  */
    drawOneLine (150.0, 100.0, 250.0, 100.0)
    glLineStipple (1, 0x1C47)  #/*  dash/dot/dash  */
    drawOneLine (250.0, 100.0, 350.0, 100.0)
    glLineWidth (1.0)
    
    #/* in 3rd row, 6 lines, with dash/dot/dash stipple  */
    #/* as part of a single connected line strip         */
    glLineStipple (1, 0x1C47)  #/*  dash/dot/dash  */
    glBegin (GL_LINE_STRIP)
    for i in range(7):
        glVertex (50.0 + i * 50.0, 75.0)
        
    glEnd()
    
    #/* in 4th row, 6 independent lines with same stipple  */
    for i in range(6):
        drawOneLine (50.0 + i * 50.0, 50.0, 50.0 + (i+1) * 50.0, 50.0)

    #/* in 5th row, 1 line, with dash/dot/dash stipple    */
    #/* and a stipple repeat factor of 5                  */
    glLineStipple (5, 0x1C47)  #/*  dash/dot/dash  */
    drawOneLine (50.0, 25.0, 350.0, 25.0)
    
    glDisable (GL_LINE_STIPPLE)
    glFlush ()
    glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0.0, w, 0.0, h);
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 150)
    glutInitWindowPosition (100, 100)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__': main()
