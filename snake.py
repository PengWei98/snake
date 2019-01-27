import pygame, sys
import pygame.freetype
import random

pygame.init()
size = width, height = (600, 400)
screen = pygame.display.set_mode(size, pygame.NOFRAME)
WHITE = 255, 255, 255
GREY = 190, 190, 190
BLACK = 0, 0, 0
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')

pygame.display.set_caption("贪吃蛇") #设置标题

icon = pygame.image.load("greedy_snake.jpg")
icon = pygame.transform.scale(icon, (300, 300))
pygame.display.set_icon(icon) #设置图标

f = pygame.freetype.Font("msyh.ttc", 36) #设置字体

playing = False #标明游戏是否正在进行

fps = 5
fclock = pygame.time.Clock()

dirc = 'L'

score = 0

v = 5

(x, y) = (-1, -1)

screen.fill(WHITE)
pygame.draw.rect(screen, GREEN, [430, 100, 120, 50])
pygame.draw.rect(screen, GREEN, [430, 240, 120, 50])
f1surf, f1rect = f.render("开始游戏", fgcolor = WHITE, size = 25)
screen.blit(f1surf, (440, 110))
f2surf, f2rect = f.render("退出游戏", fgcolor = WHITE, size = 25)
screen.blit(f2surf, (440, 250))

screen.blit(icon, (80,50))

def ge_food(snake):
    x = 10 * random.randint(1, 58)
    y = 10 * random.randint(1, 38)
    while (x, y) in snake:
        x = 10 * random.randint(1, 58)
        y = 10 * random.randint(1, 38)
    pygame.draw.rect(screen, WHITE, [x, y, 10, 10])
    return (x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_UP and dirc != 'D':
                dirc = 'U'
            elif event.key == pygame.K_DOWN and dirc != 'U':
                dirc = 'D'
            elif event.key == pygame.K_LEFT and dirc != 'R':
                dirc = 'L'
            elif event.key == pygame.K_RIGHT and dirc != 'L':
                dirc = 'R'
        if event.type == pygame.MOUSEBUTTONUP:
            if playing == 0:
                if event.pos[0] > 430 and event.pos[0] < 550 and event.pos[1] > 100 and event.pos[1] < 150:
                    score = 0
                    v = 5
                    fps = 5
                    playing = True
                    screen.fill(BLACK)
                    snake = [(300,200)]
                    dirc = 'L'
                    (x, y) = ge_food(snake)
                elif event.pos[0] > 430 and event.pos[0] < 550 and event.pos[1] > 240 and event.pos[1] < 290:
                    sys.exit()

    if playing == True:
        screen.fill(BLACK)
        head = snake[0]
        if dirc == 'U':
            new_head = (head[0], head[1] - 10)
            snake.insert(0, new_head)
        if dirc == 'D':
            new_head = (head[0], head[1] + 10)
            snake.insert(0, new_head)
        if dirc == 'L':
            new_head = (head[0] - 10, head[1])
            snake.insert(0, new_head)
        if dirc == 'R':
            new_head = (head[0] + 10, head[1])
            snake.insert(0, new_head)

        if new_head in snake[1:] or new_head[0] > 600 or head[0] < 0 or head[1] > 400 or head[1] < 0:
            playing = False
            screen.fill(WHITE)
            pygame.draw.rect(screen, GREEN, [430, 100, 120, 50])
            pygame.draw.rect(screen, GREEN, [430, 240, 120, 50])
            f1surf, f1rect = f.render("继续游戏", fgcolor = WHITE, size = 25)
            screen.blit(f1surf, (440, 110))
            f2surf, f2rect = f.render("退出游戏", fgcolor = WHITE, size = 25)
            screen.blit(f2surf, (440, 250))
            f3surf, f3rect = f.render("得分：{}".format(score), fgcolor = BLACK, size = 50)
            screen.blit(f3surf,(80, 100))
            f4surf, f4rect = f.render("速度：{}".format(v), fgcolor = BLACK, size = 50)
            screen.blit(f4surf,(80, 240))
        for body in snake:
            pygame.draw.rect(screen, WHITE, [body[0], body[1], 10, 10])

        if new_head == (x, y): #表示吃到食物
            (x, y) = ge_food(snake)
            fps = fps + 1
            score = score + 1
            v = v + 1
        else:
            snake.pop()
            pygame.draw.rect(screen, WHITE, [x, y, 10, 10])

        f5surf, f5rect = f.render("当前分数：{}  当前速度：{}".format(score, v), fgcolor = WHITE, size = 10)
        screen.blit(f5surf, (0,390))
    else:
        pass

    pygame.display.update()
    fclock.tick(fps)
