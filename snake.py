import pgzrun
import pygame,time,random
from pygame.locals import*
pygame.init()
pygame.display.set_caption('贪吃蛇游戏')
bg=Actor('bg')
class Snake:
    def __init__(self):
        self.snake=[Actor('snake_head'),Actor('snake_body_h'),Actor('snake_tail')]
        self.snake[0].pos=(400,400)
        self.snake[1].pos=(400,370)
        self.snake[2].pos=(400,340)
        self.angle=90
        self.time=time.time()
        self.rect=self.snake[0].pos
    def nhp(self,ohp):
        if self.angle==0:
            ohp.y-=30
        if self.angle==180:
            ohp.y+=30
        if self.angle==270:
            ohp.x-=30
        if self.angle==90:
            ohp.x+=30
        return ohp
    def move(self):
         att=self.snake[0]
         self.snake[0]=self.nhp(self.snake[0])
         for s in self.snake[1:]:#一个一个move
             s.angle,s.pos,att.angle,att.pos = s.angle,s.pos,att.angle,att.pos
    def set_image(self):
        self.snake[0].image='snake_head'
        self.snake[0].angle=self.angle
        for s in self.snake[1:-1]:
            if self.snake[self.snake.index(s)-1].angle==self.snake[self.snake.index(s)+1].angle:
                s.image='snake_body_h'
                s.angle=self.snake[self.snake.index(s)-1].angle
            else:
                s.image='snake_turn'
                s.angle=self.snake[self.snake.index(s)-1].angle
        self.snake[-1].image='snake_tail'
    def update(self,keyboard):
        if keyboard.TAB:
            try:
                f=open('top')
                a=f.read()
            except:
                f=open('top','w')
                a=''
            finally:
                f.close()
                print(a)
        if keyboard.w:
            self.angle=0
        if keyboard.s:
            self.angle=180
        if keyboard.a:
            self.angle=270
        if keyboard.d:
            self.angle=90
        if self.time-time.time()>=0.25:
            self.move()
            self.set_image()
            self.time=time.time()
        self.rect=self.snake[0].pos
    def __str__(self):
        return self.rect
    def draw(self):
        for s in self.snake:
             s.draw()
class Eat:
    def __init__(self):
        self.pos=(random.randint(0,600),random.randint(0,800))
        self.angle=0
        self.time=time.time()
        self.actors=[]
    def update(self):
        if self.time-time.time()>=0.25:
            for a in self.actors:
                a.angle+=1
                if a.pos==s.__str__():
                    self.actors.remove(a)
            for i in range(0,10):
                self.angles.append(Actor('snake_food'))
    def draw(self):
        for a in self.actors:
            a.draw()
s=Snake()
e=Eat()
def update():
    for event in pygame.event.get():
        if event==QUIT:
            exit()
    s.update(keyboard)
    e.update()
def draw():
    bg.draw()
    s.draw()
    e.draw()
pgzrun.go()