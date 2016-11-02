# From http://www.glprogramming.com/red/chapter01.html

#from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pygame
from pygame.locals import *
import time
import sys


spin = 0.0
lastCounter = 0.0
red = 1
green = 1
blue = 1
ired = 1/70
igreen = 1/110
iblue = 1/130

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def display():
    global spin
    global red
    global green
    global blue
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotate(spin, 0.0, 0.0, 1.0)
    glColor(red, green, blue)
    glRectf(-25.0, -25.0, 25.0, 25.0)
    glPopMatrix()
    #glutSwapBuffers()
    pygame.display.flip()

def spinDisplay():
    global lastCounter
    global spin
    global red
    global green
    global blue
    global ired
    global igreen
    global iblue
        
    counter = time.perf_counter()
    elapsedTime = counter - lastCounter
    if elapsedTime < 1/60:
        return
        
    red = red + ired
    green = green + igreen
    blue = blue + iblue
    if red>1 or red<0:
        red=max(0,min(1,red))
        ired=-ired
    if green>1 or green <0:
        green=max(0,min(1,green))
        igreen=-igreen
        
    if blue>1 or blue<0:
        blue=max(0,min(1,blue))
        iblue=-iblue

    lastCounter = counter
    spin = spin + 2.0
    if spin > 360.0:
        spin = spin - 360.0
    #glutPostRedisplay()
    display()

def reshape(w, h):
    glViewport (0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def mouse(button, state, x, y):
    if button == 1:
        if state == MOUSEBUTTONDOWN:
            #glutIdleFunc(spinDisplay)
            pass
    if button == 3:
        if state == MOUSEBUTTONDOWN:
            #glutIdleFunc()
            pass

def pygameMainLoop():
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return
            if event.type in (MOUSEBUTTONDOWN, MOUSEBUTTONUP):
                mouse(event.button, event.type, event.pos[0], event.pos[1])
            if event.type == VIDEORESIZE:
                reshape(event.size[0], event.size[1])

        #display()
        spinDisplay()
#/* 
# *  Request double buffer display mode.
# *  Register mouse input callback functions
# */

def main():
    global lastCounter
    lastCounter = time.perf_counter()
    #glutInit(sys.argv)
    #glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
    #glutInitWindowSize (250, 250)
    #glutInitWindowPosition (100, 100)
    #glutCreateWindow (b'Double')
    pygame.init()
    screen = pygame.display.set_mode( (400,400) , HWSURFACE|OPENGL|DOUBLEBUF)
    reshape(400,400)
    
    init ()

    #glutReshapeFunc(reshape)
    #glutMouseFunc(mouse)
    pygameMainLoop()
    return


if __name__ == '__main__': main()
