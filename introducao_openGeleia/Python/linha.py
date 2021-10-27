from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(0, 256, 0, 256, -1, 1)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(4.0)
    glBegin(GL_LINES)
    glVertex2i(40, 200)
    glVertex2i(200, 10)
    glEnd()
    glFlush()


def keyboard(key, x, y):
    if ord(key) == 27:
        glutLeaveMainLoop()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(256, 256)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Desenhando uma linha")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
