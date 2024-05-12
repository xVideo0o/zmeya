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
        self.rect.x = randint(5, 700-5-self.rect.width)
        self.rect.y = randint(5, 500-5-self.rect.height)
        self.image = choice(self.images)


window = display.set_mode((700,500))
back = (175, 227, 226)
display.set_caption('Змейка')
clock = time.Clock()
FPS = 40


my_food = Food('ananas.png', 100, 100, 40, 40, 0)
my_food.add_image('apelsin.png')
my_food.add_image('tomato.png')

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_q:
            my_food.new_position()



    window.fill(back)
    my_food.reset()

    display.update()
    clock.tick(FPS)