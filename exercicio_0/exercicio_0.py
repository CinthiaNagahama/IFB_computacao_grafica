from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import random

from betta_fish import draw_betta_fish
from forms import draw_circle, draw_square

height = 500
width = 500
ratio = 1

isWireFrame = False

pos = []


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, 100, 0, 100, -1, 1)


def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # Desenha um peixe
    glViewport(0, 0, int(width), int(height))

    glPushMatrix()
    glTranslatef(10, 90, 0)
    glColor(0, 0, 0)
    glScalef(0.05, 0.05, 0)
    glLineWidth(2)
    glutStrokeCharacter(GLUT_STROKE_ROMAN, 49)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(35, 45, 0)
    glScalef(1, 1, 0)
    draw_betta_fish(isWireFrame)
    glPopMatrix()

    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2f(100 * ratio, height)
    glVertex2f(100 * ratio, 0)
    glEnd()
    glLineWidth(1)

    # Cria círculos/quadrados com clique
    glViewport(int(width), 0, int(width), int(height))

    for x, y, color, form in pos:
        glColor(color)

        if form == 0:
            draw_circle(x, y, isWireFrame)
        else:
            draw_square(x, y)

    glPushMatrix()
    glTranslatef(10, 90, 0)
    glColor(0, 0, 0)
    glScalef(0.05, 0.05, 0)
    glLineWidth(2)
    glutStrokeCharacter(GLUT_STROKE_ROMAN, 50)
    glPopMatrix()

    glFlush()


def reshape(w, h):
    global width
    width = w / 2

    global height
    height = h

    global ratio

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h):
        ratio = height / width
        glOrtho(0, 100, 0, 100 * ratio, -1.0, 1.0)
    else:
        ratio = width / height
        glOrtho(0, 100 * ratio, 0, 100, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, x, y):
    if ord(key) == 77 or ord(key) == 109:
        global isWireFrame

        if(isWireFrame):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        isWireFrame = not isWireFrame
        glutPostRedisplay()

    if ord(key) == 27:
        glutLeaveMainLoop()


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        viewport = None
        viewport = glGetIntegerv(GL_VIEWPORT, viewport)

        modelview = None
        modelview = glGetDoublev(GL_MODELVIEW_MATRIX, modelview)

        projection = None
        projection = glGetDoublev(GL_PROJECTION_MATRIX, projection)

        wx = x
        y = viewport[3] - y
        wy = y

        (ox, oy, _) = gluUnProject(wx, wy, 0, modelview, projection, viewport)

        color = [
            np.round(random.random(), 3),
            np.round(random.random(), 3),
            np.round(random.random(), 3)
        ]

        pos.append((ox, oy, color, random.getrandbits(1)))
        glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutCreateWindow("Exercicío de OpenGL - Cinthia M. N. Ungefehr")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMainLoop()


if __name__ == "__main__":
    main()
