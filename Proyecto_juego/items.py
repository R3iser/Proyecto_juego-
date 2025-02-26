from typing import Any
import pygame
import Constantes

class item(pygame.sprite.Sprite):

    def __init__(self,x,y,item_type, animaciones):
        pygame.sprite.Sprite.__init__(self)
        self.item_type=item_type # 0=monedas, 1=posines
        self.animaciones=animaciones
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        self.image=self.animaciones[self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

    def update(self,posicion_pantalla,jugador):
        #reposiciionamiento segun la camara 
        self.rect.x+=posicion_pantalla[0]
        self.rect.y+=posicion_pantalla[1]
        #Compreobar colision
        if self.rect.colliderect(jugador.forma):
            #monedas
            if self.item_type==0:
                jugador.score += 1
            #posion
            elif self.item_type==1:
                jugador.vida+=50
                if jugador.vida > Constantes.vida_del_jugador:
                    jugador.vida = Constantes.vida_del_jugador
            self.kill()



        cooldown_animacion=200
        self.image=self.animaciones[self.frame_index]
        if pygame.time.get_ticks()-self.update_time>cooldown_animacion:
            self.frame_index+=1
            self.update_time=pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index=0

