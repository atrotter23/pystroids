import pygame
from constants import *

def main():
    print("Starting asteroids!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0     #delta time
    #loop for drawing to screen 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black", rect=None, special_flags=0)
        pygame.display.flip()
        # decouple game speed from computer speed
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()