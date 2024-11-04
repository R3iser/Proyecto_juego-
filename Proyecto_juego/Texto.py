import pygame

class DamageText(pygame.sprite.Sprite):
    def __init__(self,x,y,damage,font,color):
        pygame.sprite.Sprite.__init__(self)
        self.image=font.render(str(damage), True, color)
        self.rect= self.image.get_rect()
        self.rect.center=(x,y)
        self.contador=0

    def update(self, posicion_pantalla):
        #repocicionar en pantalla
        self.rect.x += posicion_pantalla[0]
        self.rect.y += posicion_pantalla[1]
        self.rect.y -=2
        self.contador+=1
        if self.contador>25:
            self.kill()