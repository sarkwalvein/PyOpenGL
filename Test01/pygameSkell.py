import pygame
from pygame.locals import *
import math
from OpenGL.GL import *

def pygameDummyFun(*vartuple):
    pass

def glutInit(a):
    pygame.init()
    
def glutInitDisplayMode(a):
    global pygameMode
    if a&GLUT_DOUBLE:
        pygameMode |= DOUBLEBUF
    else:
        pygameMode &= ~DOUBLEBUF
    pass
    
def glutInitWindowSize(w, h):
    global pygameMode
    pygame.display.set_mode( (w, h) , pygameMode)

def glutInitWindowPosition(x, y):
    pass
    
def glutCreateWindow(a):
    pass
    
def glutSwapBuffers():
    pygame.display.flip()
    
pygameFunDisplay = pygameDummyFun
pygameFunIdle = pygameDummyFun
pygameFunMouse = pygameDummyFun
pygameFunReshape = pygameDummyFun
pygameMode = OPENGL|HWSURFACE
GLUT_SINGLE = 0
GLUT_DOUBLE = 1
GLUT_RGB = 2
GLUT_DEPTH = 4

def glutReshapeFunc(fun = pygameDummyFun):
    global pygameFunReshape
    pygameFunReshape = fun
    
def glutDisplayFunc(fun = pygameDummyFun):
    global pygameFunDisplay
    pygameFunDisplay = fun
    
def glutIdleFunc(fun = pygameDummyFun):
    global pygameFunIdle
    pygameFunIdle = fun
    
def glutMouseFunc(fun = pygameDummyFun):
    global pygameFunMouse
    pygameFunMouse = fun

def glutMainLoop():
    global pygameFunDisplay
    global pygameFunIdle
    global pygameFunMouse
    global pygameFunReshape
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return
            if event.type in (MOUSEBUTTONDOWN, MOUSEBUTTONUP):
                pygameFunMouse(event.button, event.type, event.pos[0], event.pos[1])
            if event.type == VIDEORESIZE:
                pygameFunReshape(event.size[0], event.size[1])

        pygameFunIdle()
        pygameFunDisplay()

def glutSolidSphere(radius, numSides, numStacks):
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
    
