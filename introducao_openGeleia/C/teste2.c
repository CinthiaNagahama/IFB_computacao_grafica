#include <GL/glut.h>

void desenhaGrade()
    {
        glColor3f(0.8f,0.8f,0.8f);
        glLineWidth(1.0f);
        glBegin(GL_LINES);
        float x = -10;
        for(;x<=10; x++)
        {
            glVertex2f(-10,x);
            glVertex2f( 10,x);
            glVertex2f(x,-10);
            glVertex2f(x, 10);
        }
        glEnd();
        glColor3f(0.0f,0.0f,0.0f);
        glLineWidth(3.0f);
        glBegin(GL_LINES);
        glVertex2f(-10,0);
        glVertex2f( 10,0);
        glVertex2f(0,-10);
        glVertex2f(0, 10);
        glEnd();
    }

void DesenhaNaTela(void)

{

    glClear(GL_COLOR_BUFFER_BIT);

    desenhaGrade();

    // Troque Aqui

    glColor3f(1.0f, 0.0f, 0.0f); // vermelho
    glPointSize(10.0f); // aumenta o tamanho dos pontos
    glBegin(GL_POINTS);
        glVertex2f(-8,-5);
        glVertex2f( 8,-5);
        glVertex2f(-8, 0);
        glVertex2f( 8, 0);
        glVertex2f(-8, 5);
        glVertex2f( 8, 5);
    glEnd();

    // Ate Aqui

    glutSwapBuffers();

}

void Inicializa (void)

{
        glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluOrtho2D(-10,10,-10,10);
        glMatrixMode(GL_MODELVIEW);

}



int main(int argc, char** argv)

{

    glutInit(&argc,argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(320,240);

    glutInitWindowPosition(100,100);

    glutCreateWindow("Primeiro Programa em OpenGL - Poligonos");

    glutDisplayFunc(DesenhaNaTela);

    Inicializa();

    glutMainLoop();

} 
