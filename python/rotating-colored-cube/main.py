# import pygame
import pygame
from pygame.locals import *

# import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

# define verticies of cube
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

# define edges of cube
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

# define surfaces of cube
surfaces = (
    (0, 1, 2, 3),
    (0, 4, 5, 1),
    (1, 5, 7, 2),
    (2, 7, 6, 3),
    (3, 6, 4, 0),
    (4, 5, 7, 6)
    )

# define some colors
colors = (
    (1, 0, 0),  # red
    (0, 1, 0),  # green
    (0, 0, 1),  # blue
    (0, 0, 0),  # black
    )

def Cube():
    glBegin(GL_QUADS)   # define surfaces of cube
    for surface in surfaces:
        i = 0
        for vertex in surface:
            glColor3fv(colors[i])
            glVertex3fv(verticies[vertex])
            i += 1
    glEnd()

    glBegin(GL_LINES)   # define lines of cube
    for edge in edges:
        for vertex in edge:  # define the line by line's verticies
            glVertex3fv(verticies[vertex])
    glEnd()             # end of definition


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)    # use OpenGL and etc.

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
