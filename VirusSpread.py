import pygame, sys
from random import choice,randint
from math import sqrt

pygame.init()
CLOCK = pygame.time.Clock()
BGCOLOR = (0,0,0)
SIZE = (600,600)
SCREEN = pygame.display.set_mode(SIZE)
SCREEN.fill(BGCOLOR)
RADIUS = 10
step = 0
pygame.display.set_caption("Virus Spread Sim")
pList = []

class Person:
    def __init__(self,x,y,color):
        self.x = x; self.y = y; self.color = color
        self.changeX = choice([-1,1]); self.changeY = choice([-1,1])
        self.draw()
        pList.append(self)
    def draw(self):
        pygame.draw.circle(SCREEN, self.color, (self.x,self.y), RADIUS)
    def erase(self):
        pygame.draw.circle(SCREEN, BGCOLOR, (self.x, self.y), RADIUS)
    def move(self,step):
        if step % randint(100,200) == 0:
            self.changeX = choice([-1,1])
            self.changeY = choice([-1,1])
        self.erase()
        self.x += self.changeX
        self.y += self.changeY
        if self.x >= SIZE[0] - RADIUS or self.x <= RADIUS:
            self.changeX = -self.changeX
        if self.y >= SIZE[1] - RADIUS or self.y <= RADIUS:
            self.changeY = -self.changeY
        self.draw()


class Susceptible(Person):
    def __init__(self,x,y):
        super().__init__(x,y,(0,0,255))

class Infectious(Person):
    def __init__(self,x,y):
        super().__init__(x,y,(255,0,0))
        self.infectionProbability = 0.5
        self.infectionRadius = 5
        self.recoverRate = 1000
        self.initStep = step
    def infect(self,other):
        if isinstance(other,Susceptible) and sqrt((self.x-other.x)**2 + (self.y-other.y)**2) <= 2*RADIUS:
            pList.append(Infectious(other.x,other.y))
            pList.remove(other)
    def heal(self):
        if step != 0 and (step - self.initStep) % self.recoverRate == 0:
            pList.append(Recovered(self.x,self.y))
            pList.remove(self)
class Recovered(Person):
    def __init__(self,x,y):
        super().__init__(x,y,(125,125,125))

#S1 = Susceptible(100,300)
I1 = Infectious(300,300)
#R = Recovered(500,300)

#create mutliple susceptible persons
for i in range(RADIUS,SIZE[0],150):
    for j in range(RADIUS,SIZE[1],150):
        pList.append(Susceptible(i,j))

running = True
while running:
    CLOCK.tick(120)
    step += 1
    for i in range(len(pList)):
        pList[i].move(step)
        if isinstance(pList[i],Infectious):
            pList[i].heal()
        for j in range(len(pList)):
            if i != j and isinstance(pList[i],Infectious):
                pList[i].infect(pList[j])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
sys.exit()