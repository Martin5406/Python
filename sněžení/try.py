import pygame
import sys
import random
import os
import pygame.mixer

class Snowfall:
    pygame.mixer.init()

    def __init__(self, **kwargs):
        pygame.init()

        # Přidání hudby
        pygame.mixer.music.load("Last Christmas.mp3")
        pygame.mixer.music.play(-1)

        self.__info = pygame.display.Info()
        self.__width = kwargs['width'] if 'width' in kwargs else self.__info.current_w
        self.__height = kwargs['height'] if 'height' in kwargs else self.__info.current_h
        self.__snowflakes_amount = kwargs['snowflakes_amount'] if 'snowflakes_amount' in kwargs else 200
        self.__bg_image = kwargs['bg_image'] if 'bg_image' in kwargs else ("tree.jpeg")
        self.__white = kwargs['white'] if 'white' in kwargs else ((250, 250, 250, 10), (240, 240, 240, 10), (230, 230, 230, 10))
        self.__caption = kwargs['caption'] if 'caption' in kwargs else "Snowfall Screensaver"
        self.__speed = kwargs['speed'] if 'speed' in kwargs else 30
        self.__snowflakes = []
        
        self.__gifts = [Gift(random.randint(0, self.__width), random.randint(0, int(self.__height * 0.3)), self.__width, self.__height) for _ in range(3)]

        self.__score = 0

        self.__surface = pygame.display.set_mode((self.__width, self.__height), pygame.SRCALPHA, pygame.RESIZABLE)
        pygame.display.set_caption(self.__caption)
        self.__bg = pygame.image.load(f"{os.path.dirname(os.path.realpath(__file__))}//img//{self.__bg_image[random.randint(0, len(self.__bg_image) - 1)]}")
        self.__bg = pygame.transform.scale(self.__bg, (self.__width, self.__height))
        pygame.mouse.set_visible(1)
        pygame.display.flip()

    def clearSnowflakef(self):
        self.__snowflakes = []

    def generateSnowflakes(self):
        for _ in range(self.__snowflakes_amount):
            self.__snowflakes.append(Snowflake(random.randint(0, self.__width), random.randint(0, self.__height), self.__width, self.__height))

    def go(self):
        self.generateSnowflakes()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for gift in self.__gifts:
                        if not gift.hidden and gift.rect.collidepoint(pygame.mouse.get_pos()):
                            self.__score += 1
                            gift.hide()  
                            self.__gifts.append(Gift(random.randint(-2, 4), self.__height , self.__width, self.__height))

            self.__surface.blit(self.__bg, (0, 0))

            for snowflake in self.__snowflakes:
                snowflake.fall(self.__width, self.__height)
                snowflake.rotate()
                snowflake.draw(self.__surface, self.__white)

            for gift in self.__gifts:
                gift.update()
                gift.draw(self.__surface)

            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {self.__score}", True, (255, 255, 255))
            self.__surface.blit(score_text, (10, 10))

            pygame.display.flip()
            pygame.time.Clock().tick(self.__speed)

class Snowflake:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__image = pygame.image.load("vlocka.png")
        self.__size = random.uniform(0.08, 0.09)
        self.__angle = 0

    def fall(self, width, height):
        fall_speed = 10

        self.__y += self.__size * fall_speed

        if self.__y > height:
            self.__y = 0
            self.__x = random.randint(0, width)
            self.__size = random.uniform(0.05, 0.09)

    def rotate(self):
        self.__angle += 1  

    def draw(self, surface, white):
        rotated_image = pygame.transform.rotate(self.__image, self.__angle)
        scaled_image = pygame.transform.scale(rotated_image, (int(self.__size * rotated_image.get_width()), int(self.__size * rotated_image.get_height())))
        surface.blit(scaled_image, (self.__x, self.__y))

class Gift:
    def __init__(self, x, y, width, height):
        self.image = pygame.image.load("gift.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.hidden = False 

    def update(self):
        if not self.hidden:
            self.rect.y += 10
            if self.rect.y > self.height:
                self.rect.y = 0
                self.rect.x = random.randint(0, self.width)

    def draw(self, surface):
        if not self.hidden:
            surface.blit(self.image, self.rect)

    def hide(self):
        self.hidden = True

snow = Snowfall(\
    caption="Sněžení",\
    width=900,\
    height=600,\
    speed=40,\
    snowflakes_amount=100,\
    bg_image=("tree.jpeg",))
snow.go()