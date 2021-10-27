from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

shoulder = 0
elbow = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()

    # Origem posicionada no ombro
    glTranslatef(-1.0, 0.0, 0.0)
    glRotatef(GLfloat(shoulder), 0.0, 0.0, 1.0)

    # Origem posicionada no ombro
    glTranslatef(1.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glutWireCube(1.0)
    glPopMatrix()

    # Origem posicionada no cotovelo
    glTranslatef(1.0, 0.0, 0.0)
    glRotatef(GLfloat(elbow), 0.0, 0.0, 1.0)
    glTranslatef(1.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glutWireCube(1.0)
    glPopMatrix()

    # Origem volta para o sistema de coordenadas original
    glPopMatrix()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, GLsizei(w), GLsizei(h))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0,  float(w) / float(h), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)


def keyboard(key, x, y):
    global shoulder
    global elbow

    if ord(key) == ord('s'):
        shoulder = (shoulder + 5) % 360
        glutPostRedisplay()
    elif ord(key) == ord('S'):
        shoulder = (shoulder - 5) % 360
        glutPostRedisplay()
    elif ord(key) == ord('e'):
        elbow = (elbow + 5) % 360
        glutPostRedisplay()
    elif ord(key) == ord('E'):
        elbow = (elbow - 5) % 360
        glutPostRedisplay()
    elif ord(key) == 27:
        glutLeaveMainLoop()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Arm")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
