from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import random as rd

from betta_fish import draw_betta_fish

height = 500
width = 500
ratio = 1

isWireFrame = False

pos = []  # Lista de dicionários {x: int, y: int}


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, 100, 0, 100, -1, 1)


def bola_gato(x, y, bit):
    if bit:
        glBegin(GL_TRIANGLE_FAN)
        glColor(0, 1, 1)
        glVertex2f(x, y)
        glColor(0, 1, 1)
        for point in range(101):
            angle = 2 * np.pi * point / 100
            glVertex2f(np.cos(angle) * 3 + x, np.sin(angle) * 3 + y)
        glEnd()
    else:
        glBegin(GL_QUADS)
        glColor(1, 0.5, 0.3)
        glVertex2f(x - 2.5, y - 2.5)
        glVertex2f(x - 2.5, y + 2.5)
        glVertex2f(x + 2.5, y + 2.5)
        glVertex2f(x + 2.5, y - 2.5)
        glEnd()

    glFlush()


def draw_instructions():
    instructions = [
        "Instrucoes:",
        "m -> troca representacao: colorido <-> vazio"
    ]

    enter = 0
    glColor(0.5, 0.5, 0.5)
    glLineWidth(2)
    for instruction in instructions:
        glPushMatrix()
        if width > height:
            glTranslatef(4 * ratio, 10 - enter, 0)
        else:
            glTranslatef(4, 10 * ratio - enter, 0)
        glScalef(0.02, 0.02, 0)
        for c in instruction:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(c))
        glPopMatrix()

        enter += 4

    glLineWidth(1)


def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(0, 0, int(width), int(height))

    # Escreve "1" para a viewport 1
    glPushMatrix()
    glTranslatef(10, 90, 0)
    glColor(0, 0, 0)
    glScalef(0.05, 0.05, 0)
    glLineWidth(2)
    glutStrokeCharacter(GLUT_STROKE_ROMAN, 49)
    glPopMatrix()

    # Desenha instruções
    glPushMatrix()
    draw_instructions()
    glPopMatrix()

    # Desenha um peixe
    glPushMatrix()
    glTranslatef(35, 45, 0)
    glScalef(1, 1, 0)
    draw_betta_fish(isWireFrame)
    glPopMatrix()

    # Desenha divisória
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2f(100 * ratio, height)
    glVertex2f(100 * ratio, 0)
    glEnd()
    glLineWidth(1)

    glViewport(int(width), 0, int(width), int(height))

    # Cria círculos/quadrados com clique
    glPushMatrix()
    for p in pos:
        bola_gato(p["x"], p["y"], p["bit"])
    glPopMatrix()

    # Escreve "2" para a viewport 2
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

        (ax, ay, _) = gluUnProject(wx, wy, 0, modelview, projection, viewport)

        pos.append({"x": ax, "y": ay, "bit": rd.getrandbits(1)})
        glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutCreateWindow(
        "Exercicío de OpenGL - Cinthia M. N. Ungefehr e João Vítor Rezende"
    )
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMainLoop()


if __name__ == "__main__":
    main()
