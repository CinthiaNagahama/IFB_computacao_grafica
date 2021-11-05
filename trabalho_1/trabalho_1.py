from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import random as rd

height = 500
width = 500
ratio = 1

colors = [[1, 0, 0], [1, 0.5, 0], [1, 1, 0],
          [0, 1, 0], [0, 1, 1],
          [0, 0, 1], [0.5, 0, 1], [1, 0, 1]]

random_color = [False, [0, 0, 0]]

num = 3

action_warning = ""

translate_active = {"active": False, "info": [0, 0, 0]}
rotate_active = {"active": False, "info": [0, 0, 0, 1]}
scale_active = {"active": False, "info": [1, 1, 0], "mirrored": False}


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-50, 50, -50, 50, -1, 1)


def create_warning(current_state, transformation):
    global action_warning
    if transformation == "t":
        action_warning = "Translate "
        action_warning += "ativado" if current_state else "desativado"
    elif transformation == "r":
        action_warning = "Rotate "
        action_warning += "ativado" if current_state else "desativado"
    elif transformation == "s":
        action_warning = "Scale "
        action_warning += "ativado" if current_state else "desativado"
    elif transformation == "m":
        action_warning = "Espelhar"
    elif transformation == "i":
        action_warning = "Configuracao inicial"


def draw_warning():
    global action_warning
    if len(action_warning) > 0:
        if width > height:
            glTranslatef(-48 * ratio, -48, 0)
        else:
            glTranslatef(-48, -48 * ratio, 0)
        glColor(0.5, 0.5, 0.5)
        glScalef(0.03, 0.03, 0)
        glLineWidth(2)
        for c in action_warning:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(c))
        action_warning = ""

    glLineWidth(1)


def draw_polygon():
    glBegin(GL_POLYGON)
    for i in range(num):
        if random_color[0]:
            glColor(random_color[1])
        else:
            glColor(colors[i % 8])
        angle = 2 * np.pi * i / num
        glVertex2f(np.cos(angle) * 15, np.sin(angle) * 15)
    glEnd()


def draw_instructions():
    instructions = [
        "Instrucoes:",
        "t + setas: mover poligono",
        "r + setas: rotacionar poligono",
        "s + setas: mudar o tamanho do poligono",
        "m: espelhar poligono",
        "c: mudar cor do poligono para uma cor solida aleatoria",
        "x: mudar cor do poligono para arco-iris",
        "i: retornar o poligono a configuracao originial",
        "esc: sair do programa"
    ]

    enter = 0
    glColor(0.5, 0.5, 0.5)
    glLineWidth(2)
    for instruction in instructions:
        glPushMatrix()
        if width > height:
            glTranslatef(-48 * ratio, 47 - enter, 0)
        else:
            glTranslatef(-48, 47 * ratio - enter, 0)
        glScalef(0.02, 0.02, 0)
        for c in instruction:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(c))
        glPopMatrix()

        enter += 4

    glLineWidth(1)


def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    draw_instructions()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(
        translate_active["info"][0],
        translate_active["info"][1],
        translate_active["info"][2]
    )
    glScalef(
        scale_active["info"][0],
        scale_active["info"][1],
        scale_active["info"][2]
    )
    glRotatef(
        rotate_active["info"][0],
        rotate_active["info"][1],
        rotate_active["info"][2],
        rotate_active["info"][3]
    )
    if scale_active["mirrored"]:
        glScalef(-1, 1, 0)
    draw_polygon()
    glPopMatrix()

    glPushMatrix()
    draw_warning()
    glPopMatrix()

    glFlush()


def reshape(w, h):
    global width
    width = w

    global height
    height = h

    global ratio

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h):
        ratio = height / width
        glOrtho(-50, 50, -50 * ratio, 50 * ratio, -1, 1)
    else:
        ratio = width / height
        glOrtho(-50 * ratio, 50 * ratio, -50, 50, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, mouseX, mouseY):
    global translate_active
    global rotate_active
    global scale_active

    if ord(key) == ord("t") or ord(key) == ord("T"):
        translate_active["active"] = not translate_active["active"]
        scale_active["active"] = False
        rotate_active["active"] = False
        create_warning(translate_active["active"], "t")
        glutPostRedisplay()

    elif ord(key) == ord("r") or ord(key) == ord("R"):
        rotate_active["active"] = not rotate_active["active"]
        translate_active["active"] = False
        scale_active["active"] = False
        create_warning(rotate_active["active"], "r")
        glutPostRedisplay()

    elif ord(key) == ord("s") or ord(key) == ord("S"):
        scale_active["active"] = not scale_active["active"]
        translate_active["active"] = False
        rotate_active["active"] = False
        create_warning(scale_active["active"], "s")
        glutPostRedisplay()

    elif ord(key) == ord("m") or ord(key) == ord("M"):
        scale_active["mirrored"] = not scale_active["mirrored"]
        create_warning(True, "m")
        glutPostRedisplay()

    elif ord(key) == ord("c") or ord(key) == ord("C"):
        random_color[0] = True
        if random_color[0]:
            random_color[1] = [
                round(rd.random(), 3),
                round(rd.random(), 3),
                round(rd.random(), 3)
            ]
        glutPostRedisplay()
    elif ord(key) == ord("x") or ord(key) == ord("X"):
        random_color[0] = False
        glutPostRedisplay()

    elif ord(key) == ord("i") or ord(key) == ord("I"):
        global num
        num = 3

        random_color[0] = False

        translate_active["active"] = False
        translate_active["info"] = [0, 0, 0]

        scale_active["active"] = False
        scale_active["info"] = [1, 1, 0]
        scale_active["mirrored"] = False

        rotate_active["active"] = False
        rotate_active["info"] = [0, 0, 0, 1]

        create_warning(True, "i")
        glutPostRedisplay()

    elif ord(key) == 27:
        glutLeaveMainLoop()


def special_keys(key, mouseX, mouseY):
    global num

    if key == GLUT_KEY_UP:
        if translate_active["active"]:
            translate_active["info"][1] += 5
        elif rotate_active["active"]:
            rotate_active["info"][0] -= 15
        elif scale_active["active"]:
            scale_active["info"][0] *= 1.5
            scale_active["info"][1] *= 1.5
        else:
            num += 1
        glutPostRedisplay()
    elif key == GLUT_KEY_DOWN:
        if translate_active["active"]:
            translate_active["info"][1] -= 5
        elif rotate_active["active"]:
            rotate_active["info"][0] += 15
        elif scale_active["active"]:
            scale_active["info"][0] /= 1.5
            scale_active["info"][1] /= 1.5
        else:
            if num > 3:
                num -= 1
        glutPostRedisplay()
    elif key == GLUT_KEY_LEFT:
        if translate_active["active"]:
            translate_active["info"][0] -= 5
        glutPostRedisplay()
    elif key == GLUT_KEY_RIGHT:
        if translate_active["active"]:
            translate_active["info"][0] += 5
        glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Trabalho 1 - Cinthia M. N. Ungefehr")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutMainLoop()


if __name__ == "__main__":
    main()
