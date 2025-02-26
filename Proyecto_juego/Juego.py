import pygame 
import Constantes
import Jugador
import armas
import os
import Texto
import mundo
import csv
import items


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
pygame.display.set_caption("Sobrevive ;D")

#variables
posicion_pantalla=[0,0]
nivel=1

#fuentes
font=pygame.font.Font("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\texto\\Fuente_arcade.ttf",Constantes.tamaño_fuente_disparo)
font_game_over=pygame.font.Font("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\texto\\Fuente_arcade.ttf",Constantes.tamaño_fuente_game_over)
font_reinicio=pygame.font.Font("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\texto\\Fuente_arcade.ttf",Constantes.tamaño_fuente_reinicio)
font_inicio=pygame.font.Font("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\texto\\Fuente_arcade.ttf",Constantes.tamaño_fuente_inicio)
font_titulo=pygame.font.Font("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\texto\\Fuente_arcade.ttf",Constantes.tamaño_fuente_titulo_inicio)

game_over_text=font_game_over.render('GAME OVER', True,Constantes.negro)
texto_boton_reinicio=font_reinicio.render("REINICIAR",True,Constantes.blanco )
#Botones inicio
boton_jugar=pygame.Rect(Constantes.ancho_ventana/2-100,Constantes.largo_ventana/2-50,200,50)
boton_salir=pygame.Rect(Constantes.ancho_ventana/2-100,Constantes.largo_ventana/2+50,200,50)
texto_boton_jugar=font_inicio.render("Jugar",True,Constantes.blanco)
texto_boton_salir=font_inicio.render("Salir",True,Constantes.blanco)
#pantalla de inicio
def pantalla_inicio():
    ventana.fill(Constantes.morado)
    dibujar_texto("TOMD",font_titulo,Constantes.blanco,Constantes.ancho_ventana/2-200,Constantes.largo_ventana/2-200)
    pygame.draw.rect(ventana,Constantes.violeta,boton_jugar)
    pygame.draw.rect(ventana,Constantes.violeta,boton_salir)
    ventana.blit(texto_boton_jugar,(boton_jugar.x+50,boton_jugar.y+10))
    ventana.blit(texto_boton_salir,(boton_salir.x+50,boton_salir.y+10))
    pygame.display.update()

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
    tile_image=pygame.image.load(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\fondo\\tiles_separados\\tile ({x+1}).png").convert_alpha()
    tile_image=pygame.transform.scale(tile_image,(Constantes.tile_size,Constantes.tile_size))
    tile_list.append(tile_image)
#items
posion_vida_img=[]
ruta_img_pos_vida="D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\flasks"
num_posion_imagenes=contar_elemtos(ruta_img_pos_vida)
for i in range(num_posion_imagenes):
    img=pygame.image.load(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\flasks\\flasks_1_{i}.png").convert_alpha()
    img=Escala_img(img,Constantes.Posion_vida)
    posion_vida_img.append(img)

coins_img=[]
ruta_img_coins="D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\coins" 
num_coins_imagenes=contar_elemtos(ruta_img_coins)
for i in range(num_coins_imagenes):
    img=pygame.image.load(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\caracteres\\coins\\coin_{i}.png").convert_alpha()
    img=Escala_img(img,Constantes.coins)
    coins_img.append(img)

item_imagenes=[coins_img,posion_vida_img]

def dibujar_texto(texto,fuente,color,x,y,):
    img =fuente.render(texto,True,color)
    ventana.blit(img,(x,y))

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


def resetear_mundo():
    grupo_text_damage.empty()
    grupo_balas_ice.empty()
    grupo_items.empty()
    #crear una lista de tiles vacios
    data=[]
    for fila in range(Constantes.filas):
        filas=[2]*Constantes.columnas
        data.append(filas)
    return data 

world_data=[]

for fila in range (Constantes.filas):
    filas=[5]*Constantes.columnas
    world_data.append(filas)

#cargar el archivo de mapa 
with open("D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\fondo\\mapas\\Level_1.csv",newline='')as csvfile:
    reader=csv.reader(csvfile, delimiter=';')
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y]= int(columna)

world=mundo.mundo()
world.process_data(world_data,tile_list,item_imagenes,animaciones_mops)
        
def dibujar_grind():
    for x in range(30):
        pygame.draw.line(ventana,Constantes.blanco,(x*Constantes.tile_size,0),(x*Constantes.tile_size,Constantes.largo_ventana))
        pygame.draw.line(ventana,Constantes.blanco,(0,x*Constantes.tile_size),(Constantes.ancho_ventana,x*Constantes.tile_size))
#crear jugador de la clase jugador
jugador=Jugador.jugador(50, 90,animaciones,Constantes.vida_del_jugador,1)
#lista de mop
lista_mops=[]
for mop in world.lista_mops:
    lista_mops.append(mop)
#crear un arma de la clase arma
baculo=armas.arma(imagen_baculo,imagenes_ice)
#crea gupo de sprite
grupo_text_damage=pygame.sprite.Group()
grupo_balas_ice=pygame.sprite.Group()
grupo_items=pygame.sprite.Group()
#añadir items desde la data del nivel 
for item in world.lista_item:
    grupo_items.add(item)

reloj = pygame.time.Clock()

#Boton reinicio
boton_reinicio=pygame.Rect(Constantes.ancho_ventana/2-100,Constantes.largo_ventana/2+100,200,50)

mostrar_inicio=True
run=True
while run == True:
    if mostrar_inicio==True:
        pantalla_inicio()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio=False
                if boton_salir.collidepoint(event.pos):
                    run=False
    else:
        ventana.fill(Constantes.morado)
        reloj.tick(Constantes.fps)
        if jugador.vivo ==True:
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

            posicion_pantalla,nivel_completo = jugador.movimiento(delta_x, delta_y, world.obstaculos_tiles,world.exit_tile)

            #Actualizar mapa
            world.update( posicion_pantalla)
            #Actualiza el estado del jugador
            jugador.update()
            #Actualizar estado mops
            for mop in lista_mops:
                mop.update()
                
            #Actualiza el estado del arma
            bala_ice=baculo.update(jugador)
            if bala_ice:
                grupo_balas_ice.add(bala_ice)
            for bala_ice in grupo_balas_ice:
                damage,pos_damage=bala_ice.update(lista_mops,world.obstaculos_tiles)
                if damage:
                    damage_texto=Texto.DamageText(pos_damage.centerx, pos_damage.centery,damage,font,Constantes.azul )
                    grupo_text_damage.add(damage_texto)
            #Actualiza el estado del texto de daño
            grupo_text_damage.update(posicion_pantalla)
            #Actualizar items
            grupo_items.update(posicion_pantalla,jugador)
    
        #dibujar mundo
        world.draw(ventana)
        #Dibuja al jugador
        jugador.dibujar(ventana)
        #Diujar al los mops
        for mop in lista_mops:
            if mop.vida==0:
                lista_mops.remove(mop)
            if mop.vida>0:
                mop.mops(jugador,world.obstaculos_tiles,posicion_pantalla,world.exit_tile)
                mop.dibujar(ventana)
        #dibujar el arma
        baculo.dibujar(ventana)
        #Dibujar balas 
        for bala_ice in grupo_balas_ice:
            bala_ice.dibujar(ventana)
        #Dibujar la barra de vida
        vida_jugador()
        #dibujar textos
        dibujar_texto(f"Score: {jugador.score}",font,Constantes.Amarillo,1300,5)
        #dibujar texto "nivel"
        dibujar_texto(f"Nivel: "+str(nivel),font,Constantes.blanco,Constantes.ancho_ventana/2,5)

        #dibujar textos daño
        grupo_text_damage.draw(ventana)
        #Dibujar items
        grupo_items.draw(ventana)
        #chequear si el nivel esta compleatado
        if nivel_completo == True:
            if nivel<Constantes.nivel_maximo:
                nivel+=1
                world_data= resetear_mundo()
                #cargar el archivo de mapa 
                with open(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\fondo\\mapas\\Level_{nivel}.csv",newline='')as csvfile:
                    reader=csv.reader(csvfile, delimiter=';')
                    for x, fila in enumerate(reader):
                        for y, columna in enumerate(fila):
                            world_data[x][y]= int(columna) 
            
                world=mundo.mundo()
                world.process_data(world_data,tile_list,item_imagenes,animaciones_mops)
                jugador.actualizar_cordenadas(Constantes.cordenadas[str(nivel)])
                #lista de mop
                lista_mops=[]
                for mop in world.lista_mops:
                    lista_mops.append(mop)
                #añadir items desde la data del nivel 
                for item in world.lista_item:
                    grupo_items.add(item)
        if jugador.vivo==False:
            ventana.fill(Constantes.rojo_oscuro)
            text_rect=game_over_text.get_rect(center=(Constantes.ancho_ventana/2,Constantes.largo_ventana/2))
            ventana.blit(game_over_text,text_rect)
            pygame.draw.rect(ventana,Constantes.azul,boton_reinicio)
            ventana.blit(texto_boton_reinicio,(boton_reinicio.x+40,boton_reinicio.y))
        
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
                if event.key==pygame.K_e: 
                    if world.cambiar_puerta(jugador,tile_list):
                        print("puerta cambiada")
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    Jugador.izquierda=False
                if event.key==pygame.K_RIGHT:
                    Jugador.derecha=False
                if event.key==pygame.K_UP:
                    Jugador.arriba=False
                if event.key==pygame.K_DOWN:
                    Jugador.abajo=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton_reinicio.collidepoint(event.pos)and not jugador.vivo:
                    jugador.vivo=True
                    jugador.vida=Constantes.vida_del_jugador
                    jugador.score=0
                    nivel=1
                    world_data=resetear_mundo()
                    with open(f"D:\\Programacion\\Python\\Impertita\\Primercorte\\Proyecto\\asseet\\imagenes\\fondo\\mapas\\Level_{nivel}.csv",newline='')as csvfile:
                        reader=csv.reader(csvfile, delimiter=';')
                        for x, fila in enumerate(reader):
                            for y, columna in enumerate(fila):
                                world_data[x][y]= int(columna)
                    world=mundo.mundo()
                    world.process_data(world_data,tile_list,item_imagenes,animaciones_mops)
                    jugador.actualizar_cordenadas(Constantes.cordenadas[str(nivel)])
                    #lista de mop
                    lista_mops=[]
                    for mop in world.lista_mops:
                        lista_mops.append(mop)
                    #añadir items desde la data del nivel 
                    for item in world.lista_item:
                        grupo_items.add(item)


        pygame.display.update()

pygame.quit()