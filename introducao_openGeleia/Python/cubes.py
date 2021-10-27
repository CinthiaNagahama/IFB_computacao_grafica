from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()

    # / * Cubo 1 * /
    glPushMatrix()
    glTranslatef(-2.0, 0.0, 0.0)
    glScalef(2.0, 1.0, 4.0)
    glutWireCube(1.0)
    glPopMatrix()

    # / * Cubo 2 * /
    glPushMatrix()
    glRotatef(25.0, 0.0, 0.0, 1.0)
    glTranslatef(2.0, 0.0, 0.0)
    glScalef(2.0, 1.0, 4.0)
    glutWireCube(1.0)
    glPopMatrix()

    # #  / * Cubo 3 * /
    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)
    glScalef(2.0, 1.0, 4.0)
    glutWireCube(1.0)
    glPopMatrix()

    # #  / * Cubo 4 * /
    glPushMatrix()
    glTranslatef(0.0, -2.0, 0.0)
    glScalef(2.0, 1.0, 4.0)
    glutWireCube(1.0)
    glPopMatrix()

    glPopMatrix()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, GLsizei(w), GLsizei(h))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0, float(w) / float(h), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -10.0)


def keyboard(key, x, y):
    if ord(key) == 27:
        glutLeaveMainLoop()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Cube")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
