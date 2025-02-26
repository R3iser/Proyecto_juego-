import pygame
import Constantes
import math

#Movimiento del jugador
derecha=False
izquierda=False
arriba=False
abajo=False

class jugador():
    def __init__(self, x, y, animaciones, vida,tipo):
        self.score=0
        self.vida=vida
        self.vivo=True
        self.flip=False
        self.animaciones=animaciones
        self.frame_index= 0
        self.update_time=pygame.time.get_ticks()
        self.image=animaciones[self.frame_index]
        self.forma =self.image.get_rect()
        self.forma.center=(x,y)
        self.tipo=tipo
        self.golpe=False
        self.ultimo_golpe=pygame.time.get_ticks()
        self.golpe=False
        self.ultimo_golpe=pygame.time.get_ticks()
    
    def actualizar_cordenadas(self, tupla):
        self.forma.center=(tupla[0],tupla[1])
        
    def movimiento(self, delta_x, delta_y,obstaculos_tiles,exit_tile): 
        posicion_pantalla=[0,0]
        nivel_completo=False
        if delta_x<0:
            self.flip=True
        if delta_x>0:
            self.flip=False
        self.forma.x=self.forma.x+delta_x
        for obstacle in obstaculos_tiles:
            if obstacle[1].colliderect(self.forma):
                if delta_x>0:
                    self.forma.right=obstacle[1].left
                if delta_x<0:
                    self.forma.left=obstacle[1].right
                
        self.forma.y=self.forma.y+delta_y  
        for obstacle in obstaculos_tiles:
            if obstacle[1].colliderect(self.forma):
                if delta_y>0:
                    self.forma.bottom=obstacle[1].top
                if delta_y<0:
                    self.forma.top=obstacle[1].bottom
        #logica solo aplicabe a jugador
        if self.tipo==1:
            #chequear colision con el tile de salida
            if exit_tile is not None and len(exit_tile) > 1 and exit_tile[1].colliderect(self.forma):
                nivel_completo = True
                print("nivel completado")
            #actualiza pantlla mbase a jugador, mover la izuierda o derecha
            if self.forma.right > (Constantes.ancho_ventana - Constantes.limite_pantalla):
                posicion_pantalla[0]=(Constantes.ancho_ventana-Constantes.limite_pantalla)-self.forma.right
                self.forma.right=Constantes.ancho_ventana-Constantes.limite_pantalla
            if self.forma.left < Constantes.limite_pantalla:
                posicion_pantalla[0]=Constantes.limite_pantalla-self.forma.left
                self.forma.left= Constantes.limite_pantalla
            if self.forma.bottom > (Constantes.largo_ventana - Constantes.limite_pantalla):
                posicion_pantalla[1]=(Constantes.largo_ventana-Constantes.limite_pantalla)-self.forma.bottom
                self.forma.bottom=Constantes.largo_ventana-Constantes.limite_pantalla
            if self.forma.top < Constantes.limite_pantalla:
                posicion_pantalla[1]=Constantes.limite_pantalla-self.forma.top
                self.forma.top= Constantes.limite_pantalla
            return posicion_pantalla,nivel_completo
    
    def mops(self,jugador,obstaculos_tiles,posicion_pantalla,exit_tile):
        clipped_line=()
        mop_dx=0
        mop_dy=0
        #reposicion de mop
        self.forma.x += posicion_pantalla[0]
        self.forma.y += posicion_pantalla[1]
        #linea de vision
        linea_de_vision=((self.forma.centerx, self.forma.centery),(jugador.forma.centerx, jugador.forma.centery))
        #chequear si hay optaculos en la linea de vision del mop
        for obs in obstaculos_tiles:
            if obs[1].clipline(linea_de_vision):
                clipped_line=obs[1].clipline(linea_de_vision)
        #distancia con el jugador 
        distancia=math.sqrt(((self.forma.centerx-jugador.forma.centerx)**2)+((self.forma.centery-jugador.forma.centery)**2))
        if  not clipped_line and distancia<Constantes.rango:  
            if self.forma.centerx>jugador.forma.centerx:
                mop_dx=-Constantes.velocidad_mop
            if self.forma.centerx>jugador.forma.centerx:
                mop_dx=-Constantes.velocidad_mop     
            if self.forma.centerx<jugador.forma.centerx:
                mop_dx=Constantes.velocidad_mop  
            if self.forma.centery>jugador.forma.centery:
                mop_dy=-Constantes.velocidad_mop
            if self.forma.centery<jugador.forma.centery:
                mop_dy=Constantes.velocidad_mop

        self.movimiento(mop_dx,mop_dy,obstaculos_tiles,exit_tile)
        #atacar al jugador 
        if distancia < Constantes.rango_ataque and jugador.golpe==False:
            jugador.vida-=10
            jugador.golpe=True
            jugador.ultimo_golpe=pygame.time.get_ticks()


    def update(self):
        #vida del personaje
        if self.vida<=0:
            self.vida=0
            self.vivo=False
        #cooldown para ataque mop
        golpe_cooldown=Constantes.ataque_cooldown
        if self.tipo==1:
            if self.golpe==True:
                if pygame.time.get_ticks()-self.ultimo_golpe>golpe_cooldown:
                    self.golpe=False
        cooldown_animacion=100
        self.image=self.animaciones[self.frame_index]
        if pygame.time.get_ticks()-self.update_time>=cooldown_animacion:
            self.frame_index=self.frame_index+1
            self.update_time=pygame.time.get_ticks()
        if self.frame_index>=len(self.animaciones):
            self.frame_index=0

    def dibujar(self, interfaz):
        imagen_flip=pygame.transform.flip(self.image,self.flip,False)
        interfaz.blit(imagen_flip,self.forma)
        #pygame.draw.rect(interfaz, Constantes.azul, self.forma,Constantes.escala_jugador)
