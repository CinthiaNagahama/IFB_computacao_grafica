from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def draw_circle(x, y, isWireFrame):
    if isWireFrame:
        glBegin(GL_LINE_LOOP)
        for point in range(100):
            angle = 2 * np.pi * point / 100
            glVertex2f(np.cos(angle) * 2.5 + x, np.sin(angle) * 2.5 + y)
        glEnd()
        glFlush()
    else:
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for point in range(101):
            angle = 2 * np.pi * point / 100
            glVertex2f(np.cos(angle) * 2.5 + x, np.sin(angle) * 2.5 + y)
        glEnd()
        glFlush()


def draw_square(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x + 2.5, y + 2.5)
    glVertex2f(x - 2.5, y + 2.5)
    glVertex2f(x - 2.5, y - 2.5)
    glVertex2f(x + 2.5, y - 2.5)
    glEnd()
    glFlush()
