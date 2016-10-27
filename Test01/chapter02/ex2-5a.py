#http://www.glprogramming.com/red/chapter02.html
#Example 2-5 : Line Stipple Patterns: lines.c

from OpenGL.GLU import *
from OpenGL.GL import *
import sys
sys.path.append('..')
from pygameSkell import *

lIdx = 0
lModes = [GL_POINTS,
        GL_LINES,
        GL_LINE_STRIP,
        GL_LINE_LOOP,
        GL_TRIANGLES,
        GL_TRIANGLE_STRIP,
        GL_TRIANGLE_FAN,
        GL_QUADS,
        GL_QUAD_STRIP,
        GL_POLYGON]
        
def drawOneLine(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glEnd()
    
def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    global lIdx
    global lModes
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
    
    # Polygon test
    glBegin(lModes[lIdx])
    glColor(1,0,0)
    glVertex(50, 150)
    glColor(1,1,0)
    glVertex(50, 250)
    glColor(1,1,1)
    glVertex(150, 250)
    glColor(0,1,1)
    glVertex(50, 150)
    glColor(0,0,1)
    glVertex(150, 150)
    glColor(1,0,1)
    glVertex(150, 250)
    glColor(.5,.5,.5)
    glVertex(250, 250)
    glColor(.5,1,.5)
    glVertex(150, 150)
    glColor(.5,.5,1)
    glVertex(250, 150)
    glEnd()
    
    glFlush ()
    #glutSwapBuffers()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0.0, w, 0.0, h);
    
def mouse(button, state, x, y):
    global lIdx
    global lModes
    if button == 1:
        if state == MOUSEBUTTONDOWN:
            lIdx += 1
            if lIdx >= len(lModes):
                lIdx = 0
    if button == 3:
        if state == MOUSEBUTTONDOWN:
            # lIdx -= 1
            # if lIdx < 0:
            #     lIx = len(lModes)-1
            if y <= 150:
                glEnable(GL_CULL_FACE)
                if x<=150:
                    glCullFace(GL_FRONT)
                
                if 150<x<=250:
                    glCullFace(GL_BACK)
                    
                if x>250:
                    glCullFace(GL_FRONT_AND_BACK)
            else:
                glDisable(GL_CULL_FACE)
                

    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 300)
    glutInitWindowPosition (100, 100)
    glutCreateWindow(b'')
    init ()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()

if __name__ == '__main__': main()
