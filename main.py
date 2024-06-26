from pygame import *
from random import randint, choice

class GameSprite(sprite.Sprite):
    def __init__(self, img, x,y,w,h, speed):
        super().__init__()
        self. image = transform.scale(image.load(img), (w,h))
        self.rect= self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rect.h = h
        self.rect.w = w
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Food(GameSprite):
    def __init__(self, img, x,y,w,h, speed):
        super().__init__(img, x,y,w,h, speed)
        self.images = list()
        self.images.append(self.image)

    def add_image(self, img):
        w = self.rect.width
        h = self.rect.height
        new_image = transform.scale(image.load(img), (w,h))
        self.images.append(new_image)
    def new_position(self):
        self.rect.x = randint(0, 13)*50+5
        self.rect.y = randint(1, 9)*50+5
        self.image = choice(self.images)

class Snake(GameSprite):
    def __init__(self, img, x,y,w,h, speed):
        super().__init__(img, x,y,w,h, speed)
        self.images = list()
        self.images.append(self.image)
        for i in range(3):
            self.image = transform.rotate(self.image, 90)
            self.images.append(self.image)

    def update(self, direction):
        if direction == 'left':
            self.rect.x -= self.speed
            self.image = self.images[1]
        elif direction == 'right':
            self.rect.x += self.speed
            self.image = self.images[3]
        elif direction == 'up':
            self.rect.y -= self.speed
            self.image = self.images[0]
        elif direction == 'down':
            self.rect.y += self.speed
            self.image = self.images[2]

window = display.set_mode((700,500))
back = (139, 69, 19)
display.set_caption('Змейка')
clock = time.Clock()
FPS = 2

font.init()
font1 = font.SysFont('Arial', 36)
font_win = font1.render('WIN ! ! !',1,( 0, 255, 0))
font_lose = font1.render('LOSE',1, (255, 0, 0))


my_food = Food('ananas.png', 100, 100, 40, 40, 0)
my_food.add_image('apelsin.png')
my_food.add_image('tomato.png')

head = Snake('golova.png', 350, 250, 50, 50, 50)


game = True
direction = 'stop'
finish = False
lose = False
win = False
eat = 0
snake = [head]

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_q:
            my_food.new_position()
        if e.type == KEYDOWN:
            if e.key == K_w:
                direction = 'up'
            elif e.key == K_s:
                direction = 'down'
            elif e.key == K_a:
                direction = 'left'
            elif e.key == K_d:
                direction = 'right'

    if finish != True:
        window.fill(back)
        my_food.reset()
        for i in range(len(snake)-1, 0, -1):
            snake[i].rect.x = snake[i-1].rect.x
            snake[i].rect.y = snake[i-1].rect.y
            if i == 1:
                snake[i].rect.x += 5
                snake[i].rect.y += 5
            snake[i].reset()

        head.update(direction)
        head.reset()

        if head.rect.x<50 or head.rect.x>700-40-5:
            finish = True
            lose = True
        if head.rect.y<50 or head.rect.y>500-40-5:
            finish = True
            lose = True
        if head.rect.colliderect(my_food.rect):
            my_food.new_position()
            eat += 1
            tale = Snake('xvost.png', -100, -100, 40, 40, 0)
            tale.rect.x = head.rect.x
            tale.rect.y = head.rect.y
            snake.append(tale)
            if eat>=20:
                finish = True
                win = True
            if eat % 5  == 0:
                FPS += 1

            

    if lose:
        window.blit(font_lose, (20, 45))
    if win:
        window.blit(font_win, (20, 45))
    font_score = font1.render('Скушано фруктов: '+str(eat), 1,(255, 255, 255))
    window.blit(font_score,(5,5))

    


    display.update()
    clock.tick(FPS)