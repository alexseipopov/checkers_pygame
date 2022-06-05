import pygame
import sys
from config import *

pygame.init()

SCREEN = pygame.display.set_mode(SIZE)
checker = {
    'r': pygame.transform.scale(pygame.image.load('assets/r.png'), (FIELD_SIZE, FIELD_SIZE)),
    'b': pygame.transform.scale(pygame.image.load('assets/b.png'), (FIELD_SIZE, FIELD_SIZE))
}
pos = [
    ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
    ['b', '-', 'b', '-', 'b', '-', 'b', '-'],
    ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['r', '-', 'r', '-', 'r', '-', 'r', '-'],
    ['-', 'r', '-', 'r', '-', 'r', '-', 'r'],
    ['r', '-', 'r', '-', 'r', '-', 'r', '-'],
]
fields = []

def build_fields():
    for i in range(8):
        line = []
        for j in range(8):
            line.append(pygame.Rect(j*FIELD_SIZE, i*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
        fields.append(line)


def show_field():
    for i in range(8):
        for j in range(8):
            color = (255, 255, 255)
            if (i + j) % 2 == 1:
                color = (200, 200, 200)
            pygame.draw.rect(SCREEN, color, fields[i][j])
            if pos[i][j] != '-':
                SCREEN.blit(checker[pos[i][j]], fields[i][j])
    
            


def update_screen():
    SCREEN.fill('white')
    show_field()
    pygame.display.update()


def check_events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()


def main():
    build_fields()
    while True:
        check_events()
        update_screen()

if __name__ == '__main__':
    main()