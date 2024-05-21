from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
            speed = 10
            keys_pressed = key.get_pressed()
            if keys_pressed[K_LEFT] and self.rect.x>5:
                self.rect.x-= speed
            if keys_pressed[K_RIGHT] and self.rect.x<640:
                self.rect.x+=speed
            if keys_pressed[K_UP] and self.rect.y>5:
                self.rect.y-=speed
            if keys_pressed[K_DOWN] and self.rect.y<440:
                self.rect.y+=speed
class Enemy(GameSprite):
    def update(self):
        speed = 2
        if self.rect.x>=620:
            self.direction = 'left'

        if self.rect.x<=490:
            self.direction = 'right'

        if self.direction == 'right':
            self.rect.x+=speed
        if self.direction == 'left':
            self.rect.x-=speed
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, x, y, width, height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height 
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))     
font.init()
font = font.Font(None, 70)
window = display.set_mode((700,500))
clock = time.Clock()
display.set_caption('Лабиринт')
background = transform.scale(image.load('Maze/background3.png'), (700,500))
mixer.init()
mixer.music.load('Maze/jungles.ogg')
mixer.music.play()
hero = Player('Maze/hero.png', 20, 390, 10)
cyborg = Enemy('Maze/cyborg.png', 620, 270, 2)
money = GameSprite('Maze/treasure.png', 600, 410, 0)
wall1 = Wall(100, 0, 100, 100, 10, 10, 350)
wall2 = Wall(100, 0, 100, 100, 10, 500, 10)
wall3 = Wall(100, 0, 100, 100, 480, 400, 10)
money1 = mixer.Sound('Maze/money.ogg')
Win = font.render('YOU WIN!', True, (0, 255, 0))
Lost = font.render('YOU LOST!', True, (255, 0, 0))
kick = mixer.Sound('Maze/kick.ogg')
game = True
finish = False
while game:
    if finish != True:
        window.blit(background, (0,0))
        cyborg.reset()
        cyborg.update()
        money.reset()
        hero.update()
        hero.reset()
        wall1.draw()
        wall2.draw()
        wall3.draw()
        if sprite.collide_rect(hero, money):
            window.blit(Win, (200, 200))
            finish = True
            money1.play()
        if sprite.collide_rect(hero,wall1) or sprite.collide_rect(hero,wall2) or sprite.collide_rect(hero,wall3) or sprite.collide_rect(hero,cyborg):
            window.blit(Lost, (200, 200))
            finish = True
            kick.play()
    for e in event.get():
            if e.type == QUIT:
                game = False
    clock.tick(50)
    display.update()

#создай игру "Лабиринт"!