import pygame 
import Constantes
import Jugador
import armas
import os
import Texto
import mundo
import csv

#funcion de escala
def Escala_img(imagen,escala):
    w= imagen.get_width()
    h= imagen.get_height()
    nueva_imagen=pygame.transform.scale(imagen,(w*escala,h*escala))
    return nueva_imagen
#funcion de contar elementos
def contar_elemtos(directorio):
    return len(os.listdir(directorio))
#funcion listar nombres
def nombre_carpeta(directorio):
    return os.listdir(directorio)

pygame.init()
ventana=pygame.display.set_mode((Constantes.ancho_ventana,Constantes.largo_ventana))
pygame.display.set_caption("Bienvenido a TOMD :D")

#variables
posicion_pantalla=[0,0]

#fuentes
font=pygame.font.Font("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\texto\\Fuente_arcade.ttf",Constantes.Tamaño_fuente_disparo)

#importar imagenes 
#vida
Barra_llena=pygame.image.load("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\items\Health_0.png")
Barra_llena=Escala_img(Barra_llena,Constantes.escala_barra_de_vida)
Barra_casi_llena=pygame.image.load("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\items\Health_1.png")
Barra_casi_llena=Escala_img(Barra_casi_llena,Constantes.escala_barra_de_vida)
Barra_medio_llena=pygame.image.load("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\items\Health_2.png")
Barra_medio_llena=Escala_img(Barra_medio_llena,Constantes.escala_barra_de_vida)
Barra_casi_vacia=pygame.image.load("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\items\Health_3.png")
Barra_casi_vacia=Escala_img(Barra_casi_vacia,Constantes.escala_barra_de_vida)
Barra_vacia=pygame.image.load("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\items\Health_4.png")
Barra_vacia=Escala_img(Barra_vacia,Constantes.escala_barra_de_vida)
#personaje
animaciones=[]
for i in range(8):
    imagenes=pygame.image.load(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\player\\Movimiento_1_{i}.png")
    imagenes=Escala_img(imagenes, Constantes.escala_jugador)
    animaciones.append(imagenes)
#mops
directorio_mops="D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\mops"
tipo_mops=nombre_carpeta(directorio_mops)
animaciones_mops=[]
for mp in tipo_mops:
    lista_temporal=[]
    ruta_temp=f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\mops\\{mp}"
    num_animaciones=contar_elemtos(ruta_temp)
    for i in range(num_animaciones):
        img_mop=pygame.image.load(f"{ruta_temp}\\{mp}_{i}.png").convert_alpha()
        img_mop=Escala_img(img_mop,Constantes.escala_mop)
        lista_temporal.append(img_mop)
    animaciones_mops.append(lista_temporal)

#armas
imagen_baculo=pygame.image.load(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\arma\\baculo_3.png").convert_alpha()
imagen_baculo=Escala_img(imagen_baculo,Constantes.escala_arma_prinsipal )
#municion ice
imagenes_ice=pygame.image.load(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\municion\\ICE_1_5.png").convert_alpha()
imagenes_ice=Escala_img(imagenes_ice, Constantes.escala_municion)
#mundo
tile_list=[]
for x in range (Constantes.tiles_types):
    tile_image=pygame.image.load(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\fondo\\tiles_separados\\tile ({x+1}).png")
    tile_image=pygame.transform.scale(tile_image,(Constantes.tile_size,Constantes.tile_size))
    tile_list.append(tile_image)

def vida_jugador():
    porcentaje_vida = jugador.vida / Constantes.vida_del_jugador
    if porcentaje_vida >= 1.0:
        ventana.blit(Barra_llena, (5, 5)) 
    elif porcentaje_vida >= 0.7:
        ventana.blit(Barra_casi_llena, (5, 5))  
    elif porcentaje_vida >= 0.4:
        ventana.blit(Barra_medio_llena, (5, 5))  
    elif porcentaje_vida >= 0.1:
        ventana.blit(Barra_casi_vacia, (5, 5)) 
    else:
        ventana.blit(Barra_vacia, (5, 5))



world_data=[]

for fila in range (Constantes.filas):
    filas=[79]*Constantes.columnas
    world_data.append(filas)

#cargar el archivo de mapa 
with open("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\fondo\\mapas\\Level_1.csv",newline='')as csvfile:
    reader=csv.reader(csvfile, delimiter=';')
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y]= int(columna)

world=mundo.mundo()
world.process_data(world_data,tile_list)
        
def dibujar_grind():
    for x in range(30):
        pygame.draw.line(ventana,Constantes.blanco,(x*Constantes.tile_size,0),(x*Constantes.tile_size,Constantes.largo_ventana))
        pygame.draw.line(ventana,Constantes.blanco,(0,x*Constantes.tile_size),(Constantes.ancho_ventana,x*Constantes.tile_size))

#crear jugador de la clase jugador
jugador=Jugador.jugador(50, 90,animaciones,Constantes.vida_del_jugador,1)
#crear mop de la clase personaje
esqueleto_intermedio=Jugador.jugador(200,350,animaciones_mops[0],400,2)
esqueleto_normal=Jugador.jugador(300,600,animaciones_mops[1],200,2)
#lista de mop
lista_mops=[]
lista_mops.append(esqueleto_intermedio)
lista_mops.append(esqueleto_normal)
#crear un arma de la clase arma
baculo=armas.arma(imagen_baculo,imagenes_ice)
#crea gupo de sprite
grupo_text_damage=pygame.sprite.Group()
grupo_balas_ice=pygame.sprite.Group()

reloj = pygame.time.Clock()
run=True
while run == True:
    ventana.fill(Constantes.gris)
    reloj.tick(Constantes.fps)
    dibujar_grind()
    delta_x=0
    delta_y=0
    #Movimiento del jugador
    if Jugador.derecha==True:
        delta_x=Constantes.velocidad_por_pixel
    if Jugador.izquierda==True:
        delta_x=-Constantes.velocidad_por_pixel
    if Jugador.arriba==True:
        delta_y=-Constantes.velocidad_por_pixel
    if Jugador.abajo==True:
        delta_y=Constantes.velocidad_por_pixel

    posicion_pantalla=jugador.movimiento(delta_x,delta_y,world.obstaculos_tiles )

    #Actualizar mapa
    world.update( posicion_pantalla)
    #Actualiza el estado del jugador
    jugador.update()
    #Actualizar estado mops
    for mop in lista_mops:
        mop.mops(posicion_pantalla)
        mop.update()
        
    #Actualiza el estado del arma
    bala_ice=baculo.update(jugador)
    if bala_ice:
        grupo_balas_ice.add(bala_ice)
    for bala_ice in grupo_balas_ice:
        damage,pos_damage=bala_ice.update(lista_mops)
        if damage:
            damage_texto=Texto.DamageText(pos_damage.centerx, pos_damage.centery,damage,font,Constantes.azul )
            grupo_text_damage.add(damage_texto)
    #Actualiza el estado del texto de daño
    grupo_text_damage.update(posicion_pantalla)

    #dibujar mundo
    world.draw(ventana)
    #Dibuja al jugador
    jugador.dibujar(ventana)
    #Diujar al los mops
    for mop in lista_mops:
        mop.dibujar(ventana)
    #dibujar el arma
    baculo.dibujar(ventana)
    #Dibujar balas 
    for bala_ice in grupo_balas_ice:
        bala_ice.dibujar(ventana)
    #Dibujar la barra
    vida_jugador()
    #dibujar textos daño
    grupo_text_damage.draw(ventana)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                Jugador.izquierda=True
            if event.key==pygame.K_RIGHT:
                Jugador.derecha=True
            if event.key==pygame.K_UP:
                Jugador.arriba=True
            if event.key==pygame.K_DOWN:
                Jugador.abajo=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                Jugador.izquierda=False
            if event.key==pygame.K_RIGHT:
                Jugador.derecha=False
            if event.key==pygame.K_UP:
                Jugador.arriba=False
            if event.key==pygame.K_DOWN:
                Jugador.abajo=False

    pygame.display.update()

pygame.quit()