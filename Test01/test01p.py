# From http://code.activestate.com/recipes/325391-open-a-glut-window-and-draw-a-sphere-using-pythono/

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys
import pygame
from pygame.locals import *

name = b'ball_glut'

def pygameMainLoop():
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return                

        #time_passed = clock.tick()
        #time_passed_seconds = time_passed / 1000.
        
        pressed = pygame.key.get_pressed()
        
        display()
    
def main():
    # glutInit(sys.argv)
    # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # glutInitWindowSize(400,400)
    # glutCreateWindow(name)

    pygame.init()
    screen = pygame.display.set_mode( (400,400) , HWSURFACE|OPENGL|DOUBLEBUF)

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    #glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    # glutMainLoop()
    pygameMainLoop()
    return

def grootSolidSphere(radius, numSides, numStacks):
    numVerts = (numStacks-1)*numSides;
    points = [0 for x in range(numVerts)]
    curVert = 0
    M_PI = 3.14159265

    deltaTheta = (2*M_PI) / numSides;
    deltaRho = M_PI / numStacks

    for curStack in range(1, numStacks):
        curRho = (3.141/2.0) - curStack*deltaRho
        curY = math.sin(curRho) * radius
        curRadius = math.cos(curRho) * radius
        for curSlice in range(numSides):
            curTheta = curSlice * deltaTheta
            curX = curRadius * math.cos(curTheta)
            curZ = -curRadius * math.sin(curTheta)
            points[curVert] = [curX,curY,curZ]
            curVert+=1

    # part A - draw the top 'lid' (tris)
    glBegin(GL_TRIANGLE_FAN)
    glNormal(0,1,0)
    glVertex(0,radius,0);
    for t in range(numSides):
        curX = points[t][0]
        curY = points[t][1]
        curZ = points[t][2]
        glNormal(curX, curY, curZ)
        glVertex(curX, curY, curZ)

    curX = points[0][0]
    curY = points[0][1]
    curZ = points[0][2]
    glNormal(curX, curY, curZ)
    glVertex(curX, curY, curZ)
    glEnd()

    # part B - draw the 'sides' (quads)
    for curStack in range(numStacks-2):
        vertIndex = curStack * numSides
        glBegin(GL_QUAD_STRIP)
        for curSlice in range(numSides):
            glNormal(points[vertIndex+curSlice][0], points[vertIndex+curSlice][1], points[vertIndex+curSlice][2])
            glVertex(points[vertIndex+curSlice][0], points[vertIndex+curSlice][1], points[vertIndex+curSlice][2])

            glNormal(points[vertIndex+numSides+curSlice][0], points[vertIndex+numSides+curSlice][1], points[vertIndex+numSides+curSlice][2])
            glVertex(points[vertIndex+numSides+curSlice][0], points[vertIndex+numSides+curSlice][1], points[vertIndex+numSides+curSlice][2])

        glNormal(points[vertIndex][0], points[vertIndex][1], points[vertIndex][2])
        glVertex(points[vertIndex][0], points[vertIndex][1], points[vertIndex][2])
        glNormal(points[vertIndex+numSides][0], points[vertIndex+numSides][1], points[vertIndex+numSides][2])
        glVertex(points[vertIndex+numSides][0], points[vertIndex+numSides][1], points[vertIndex+numSides][2])
        glEnd()

    # part C - draw the bottom 'lid' (tris)
    glBegin(GL_TRIANGLE_FAN)
    glNormal(0,-1,0)
    glVertex(0,-radius,0)
    for t in range(numSides-1):
        curX = points[numVerts-1-t][0]
        curY = points[numVerts-1-t][1]
        curZ = points[numVerts-1-t][2]
        glNormal(curX, curY, curZ)
        glVertex(curX, curY, curZ)
    
    curX = points[numVerts-1][0]
    curY = points[numVerts-1][1]
    curZ = points[numVerts-1][2]
    glNormal(curX, curY, curZ)
    glVertex(curX, curY, curZ)
    glEnd()
    
    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0,0.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    #glutSolidSphere(2,20,20)
    grootSolidSphere(2,20,20)
    glPopMatrix()
    #glutSwapBuffers()
    pygame.display.flip()
    return

if __name__ == '__main__': main()

