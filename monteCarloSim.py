from random import randint
import pygame, sys
from math import sqrt

a,b = 0,800
domain = [a,b]
#domain limits of what x and y of a random point can be

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Monte Carlo")
screen.fill((255,255,255))
clock = pygame.time.Clock()
pygame.draw.circle(screen, (255,0,0), (0,0), 800, 0)

insideCircle = []
notInsideCircle = []

count = 0
running = True
print("Approximating pi...")
while running:
    count+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    point = [randint(a,b),randint(a,b)]
    dist = sqrt(point[0]**2 + point[1]**2)
    if dist > 800:
        notInsideCircle.append(point)
        pygame.draw.circle(screen, (0, 0, 0), (point[0], point[1]), 2, 0)
    else:
        insideCircle.append(point)
        pygame.draw.circle(screen, (0, 255, 0), (point[0], point[1]), 2, 0)
    ratio = len(insideCircle)/count
    if count%10 == 0:
        print(ratio*4)

    pygame.display.update()
    
pygame.quit()

print(f"Final approximation of pi: {ratio*4}")

sys.exit()