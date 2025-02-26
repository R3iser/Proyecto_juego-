from typing import Any
import pygame
from pygame.sprite import Group
import Constantes
import math
import random
import mundo

class arma():
    def __init__(self,image,imagen_bala):
        self.imagen_bala=imagen_bala
        self.imagen_original=image
        self.angulo=0
        self.imagen=pygame.transform.rotate(self.imagen_original,self.angulo)
        self.forma=self.imagen.get_rect()
        self.disparo = False
        self.ultimo_disparo=pygame.time.get_ticks()
    
    def update(self,jugador):
        disparo_cooldown=Constantes.disparo_cooldown
        bala_ice=None
        self.forma.center=jugador.forma.center
        if jugador.flip==False:
            self.forma.x +=  jugador.forma.width/6
            self.forma.y +=  15
            self.rotar_arma(False)
        if jugador.flip==True:
            self.forma.x -=  jugador.forma.width/6
            self.forma.y +=  15
            self.rotar_arma(True)
        #movimiento de la pistola
        mouse_pos=pygame.mouse.get_pos()
        distancia_x=mouse_pos[0]-self.forma.centerx
        distancia_y=-(mouse_pos[1]-self.forma.centery)
        self.angulo=math.degrees(math.atan2(distancia_y,distancia_x))

        #detectar clik 
        if pygame.mouse.get_pressed()[0] and self.disparo ==False and (pygame.time.get_ticks()-self.ultimo_disparo >= disparo_cooldown):
            bala_ice=municion_ice(self.imagen_bala,self.forma.centerx, self.forma.centery,self.angulo )
            self.disparo= True
            self.ultimo_disparo=pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0]==False:
            self.disparo = False
        return bala_ice 
    
    def rotar_arma(self, rotar):
        if rotar ==True:
            imagen_flip=pygame.transform.flip(self.imagen_original,True,False)
            self.imagen=pygame.transform.rotate(imagen_flip,self.angulo)
        else:
            imagen_flip=pygame.transform.flip(self.imagen_original,False,False)
            self.imagen=pygame.transform.rotate(imagen_flip,self.angulo)

    def dibujar(self,interfaz):
        self.imagen=pygame.transform.rotate(self.imagen,self.angulo)
        interfaz.blit(self.imagen,self.forma)
        #pygame.draw.rect(interfaz,Constantes.blanco, self.forma, 1)
    


class municion_ice(pygame.sprite.Sprite):
    def __init__(self,image,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original=image
        self.angulo=angle
        self.image=pygame.transform.rotate(self.imagen_original,self.angulo)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        #calculo de la veocidad de la bala
        self.delta_x=math.cos(math.radians(self.angulo))*Constantes.velocidad_ice_bala
        self.delta_y=-math.sin(math.radians(self.angulo))*Constantes.velocidad_ice_bala

    def update(self,lista_mops,obstaculos_tile):
        damage=0
        pos_damage=None
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y
        if self.rect.right<0 or self.rect.right>Constantes.ancho_ventana or self.rect.bottom<0 or self.rect.top > Constantes.largo_ventana:
            self.kill()
        #verificar colision
        for mops in lista_mops:
            if mops.forma.colliderect(self.rect):
                damage=25+random.randint(-10,10)
                pos_damage=mops.forma
                mops.vida-=damage
                self.kill()
                break
        #Verificar colicion con paredes 
        for obs in obstaculos_tile:
            if obs[1].colliderect(self.rect):
                self.kill()
                break
        return damage, pos_damage
    
    def dibujar(self,interfaz):
        interfaz.blit(self.image, (self.rect.centerx,self.rect.centery-int(self.image.get_height()/2)))