# Slide: OpenGL - figuras compostas

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

X = 0
Y = 0


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-256, 256, -256, 256, -1, 1)


def nose():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(X - 10.0, Y, 0.0)
    glVertex3f(X, Y + 20, 0.0)
    glVertex3f(X + 10, Y, 0.0)
    glEnd()


def body():
    glBegin(GL_QUADS)
    glColor3f(.0, .0, 1.0)
    glVertex3f(X - 7.0, Y, 0.0)
    glVertex3f(X + 7.0, Y, 0.0)
    glVertex3f(X + 7.0, Y - 40.0, 0.0)
    glVertex3f(X - 7.0, Y - 40.0, 0.0)
    glEnd()


def left_fin():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(X - 14, Y - 40.0, 0.0)
    glVertex3f(X - 7, Y - 40.0, 0.0)
    glVertex3f(X - 7, Y - 25.0, 0.0)
    glEnd()


def right_fin():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(X + 14, Y - 40, 0.0)
    glVertex3f(X + 7, Y - 40, 0.0)
    glVertex3f(X + 7, Y - 25, 0.0)
    glEnd()


def draw_rocket():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    nose()
    body()
    left_fin()
    right_fin()
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h):
        glOrtho(-50.0, 50.0, -50.0 * h / w, 50.0 * h / w, -1.0, 1.0)
    else:
        glOrtho(-50.0 * w / h, 50.0 * w / h, -50.0, 50.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, x, y):
    if ord(key) == 119 or ord(key) == 87:  # w | W
        glTranslatef(0, 5, 0)
        glutPostRedisplay()
    elif ord(key) == 97 or ord(key) == 65:  # a | A
        glTranslatef(-5, 0, 0)
        glutPostRedisplay()
    elif ord(key) == 115 or ord(key) == 83:  # s | S
        glTranslatef(0, -5, 0)
        glutPostRedisplay()
    elif ord(key) == 100 or ord(key) == 68:  # d | D
        glTranslatef(5, 0, 0)
        glutPostRedisplay()

    elif ord(key) == 101 or ord(key) == 69:  # e | E
        glRotatef(-15, 0, 0, 1)
        glutPostRedisplay()
    elif ord(key) == 113 or ord(key) == 81:  # q | Q
        glRotatef(15, 0, 0, 1)
        glutPostRedisplay()

    elif ord(key) == 120 or ord(key) == 88:  # x | X
        glScalef(.5, .5, 0)
        glutPostRedisplay()
    elif ord(key) == 99 or ord(key) == 67:  # c | C
        glScalef(2, 2, 0)
        glutPostRedisplay()

    elif ord(key) == 27 or ord(key) == 122 or ord(key) == 90:  # z | Z
        glutLeaveMainLoop()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Rocket")
    init()
    glutDisplayFunc(draw_rocket)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
