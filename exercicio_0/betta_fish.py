from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

cinza = [0.509, 0.509, 0.529]
vermelho_1 = [0.490, 0.090, 0.070]
vermelho_2 = [0.635, 0.160, 0.098]


def draw_half_moon_betta_fish_eye_filled():
    glBegin(GL_TRIANGLE_FAN)
    glColor(cinza)
    glVertex2f(-14.5, 1)
    glColor3f(0, 0, 0)
    for point in range(101):
        angle = 2 * np.pi * point / 100
        glVertex2f(np.cos(angle) * 1.6 - 14.5, np.sin(angle) * 1.6 + 1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    for point in range(100):
        angle = 2 * np.pi * point / 100
        glVertex2f(np.cos(angle) * 1.6 - 14.5, np.sin(angle) * 1.6 + 1)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-14.5, 1)
    for point in range(101):
        angle = 2 * np.pi * point / 100
        glVertex2f(np.cos(angle) * 0.75 - 14.5, np.sin(angle) * 0.72 + 1)
    glEnd()


def draw_half_moon_betta_fish_eye_hollow():
    glBegin(GL_LINE_LOOP)
    glColor(cinza)
    for point in range(100):
        angle = 2 * np.pi * point / 100
        glVertex2f(np.cos(angle) * 1.6 - 14.5, np.sin(angle) * 1.6 + 1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    for point in range(100):
        angle = 2 * np.pi * point / 100
        glVertex2f(np.cos(angle) * 0.75 - 14.5, np.sin(angle) * 0.72 + 1)
    glEnd()


def draw_half_moon_betta_fish_body():
    glBegin(GL_TRIANGLE_STRIP)

    glColor(vermelho_1)
    glVertex2f(-18, 2)
    glVertex2f(-15, 3.5)
    glVertex2f(-16, -2)

    glColor(vermelho_1)
    glVertex2f(-10, 7)

    glColor(vermelho_1)
    glVertex2f(-10, -5)

    glColor(vermelho_1)
    glVertex2f(2, 12)

    glColor3f(0, 0, 0)
    glVertex2f(1, -6)

    glColor(vermelho_1)
    glVertex2f(12, 14)

    glColor3f(0, 0, 0)
    glVertex2f(20, -3)

    glColor(vermelho_1)
    glVertex2f(24, 12)

    glColor3f(0, 0, 0)
    glVertex2f(30, 2)

    glColor(vermelho_1)
    glVertex2f(31, 10)
    glEnd()


def draw_half_moon_betta_fish_dorsal_fin():
    glBegin(GL_QUADS)

    glColor(vermelho_2)
    glVertex2f(12, 14)
    glVertex2f(9, 22)
    glColor3f(0, 0, 0)
    glVertex2f(14, 28)
    glColor(vermelho_2)
    glVertex2f(15, 13.5)

    glEnd()

    glBegin(GL_QUAD_STRIP)

    glColor(vermelho_2)
    glVertex2f(14, 13.5)
    glColor3f(0, 0, 0)
    glVertex2f(14, 33)
    glColor(vermelho_2)
    glVertex2f(21, 12.45)
    glColor3f(0, 0, 0)
    glVertex2f(22, 36)

    glColor(vermelho_2)
    glVertex2f(24, 12)
    glColor3f(0, 0, 0)
    glVertex2f(30, 32)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glColor(vermelho_2)
    glVertex2f(24, 12)
    glColor3f(0, 0, 0)
    glVertex2f(29.4, 30)
    glVertex2f(34, 25)

    glVertex2f(37, 20)

    glVertex2f(38, 15)

    glVertex2f(36.5, 10)

    glVertex2f(35, 8)

    glEnd()


def draw_half_moon_betta_fish_pectoral_fin():
    glBegin(GL_QUADS)

    glColor3f(0, 0, 0)
    glVertex2f(-2, -5)
    glColor(vermelho_1)
    glVertex2f(-6, -10)
    glVertex2f(-2, -16)
    glVertex2f(4, -10)

    glEnd()


def draw_half_moon_betta_fish_pelvic_fin():
    glBegin(GL_QUAD_STRIP)

    glColor3f(0, 0, 0)
    glVertex2f(2, -15)

    glColor(vermelho_2)
    glVertex2f(2.5, -5.5)
    glColor3f(0, 0, 0)
    glVertex2f(7, -17)
    glColor(vermelho_2)
    glVertex2f(8, -4.9)

    glColor3f(0, 0, 0)
    glVertex2f(18.5, -18)
    glColor(vermelho_2)
    glVertex2f(18, -3.3)

    glColor3f(0, 0, 0)
    glVertex2f(25.5, -15)
    glColor(vermelho_2)
    glVertex2f(25, -0.5)

    glColor3f(0, 0, 0)
    glVertex2f(30.5, -7)
    glColor(vermelho_2)
    glVertex2f(27, 0.5)

    glEnd()


def draw_half_moon_betta_fish_outer_tail():
    glBegin(GL_TRIANGLE_FAN)

    glColor(vermelho_2)
    glVertex2f(30, 8)
    glColor3f(0, 0, 0)
    glVertex2f(29, 34)
    glVertex2f(40, 33)
    glVertex2f(45, 29)
    glVertex2f(50, 25)
    glVertex2f(53, 19)
    glVertex2f(54, 10)
    glVertex2f(53, 1)
    glVertex2f(50, -5)
    glVertex2f(45, -9)
    glVertex2f(40, -13)
    glVertex2f(29, -14)

    glEnd()


def draw_betta_fish(isWireFrame):
    draw_half_moon_betta_fish_pelvic_fin()
    draw_half_moon_betta_fish_outer_tail()
    draw_half_moon_betta_fish_dorsal_fin()
    draw_half_moon_betta_fish_body()
    draw_half_moon_betta_fish_pectoral_fin()

    if isWireFrame:
        draw_half_moon_betta_fish_eye_hollow()
    else:
        draw_half_moon_betta_fish_eye_filled()
