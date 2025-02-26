import pygame
import Constantes
import items
import Jugador

obstaculos=[0,1,2,3,4,5,10,15,20,25,30,35,36,37,38,40,41,42,43,44,45,48,50,51,52,53,54,55,57,58,66,67,78]
puerta_cerrada=[36,37,38,66,67]

class mundo():
    def __init__(self):
        self.map_tiles=[]
        self.obstaculos_tiles=[]
        self.exit_tile = None
        self.lista_item=[]
        self.lista_mops=[]
        self.puertas_cerradas_tiles=[]

    def  process_data(self, data,tile_list,item_imagenes,animacion_mops):
        self.level_length =len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image=tile_list[tile]
                image_rect=image.get_rect()
                image_x=x*Constantes.tile_size
                image_y=y*Constantes.tile_size
                image_rect.center=(image_x, image_y)
                tile_data=[image,image_rect,image_x,image_y,tile ]
                #tiles a obstaculos
                if tile in obstaculos:
                    self.obstaculos_tiles.append(tile_data)
                #tile de puertas
                if tile in puerta_cerrada:
                    self.puertas_cerradas_tiles.append(tile_data)
                #tile salida
                elif tile == 56 or tile==46 or tile==94:
                    self.exit_tile = tile_data
                #crear monedas
                elif tile==86:
                    moneda=items.item(image_x,image_y,0,item_imagenes[0])
                    self.lista_item.append(moneda)
                    tile_data[0]=tile_list[16]
                #crear posiones
                elif tile==98:
                    posion=items.item(image_x,image_y,1,item_imagenes[1])
                    self.lista_item.append(posion)
                    tile_data[0]=tile_list[73]
                #crear mop esqueleto
                elif tile==68:
                    esqueleto=Jugador.jugador(image_x,image_y,animacion_mops[1],Constantes.vida_esueleto,2)
                    self.lista_mops.append(esqueleto)
                    tile_data[0]=tile_list[26]
                #crear mop esqueleto acorasado
                elif tile==77:
                    esqueleto_acorasado=Jugador.jugador(image_x,image_y,animacion_mops[0],Constantes.vida_esueleto_acorazado,2)
                    self.lista_mops.append(esqueleto_acorasado)
                    tile_data[0]=tile_list[28]
                
                #crear mop slime
                elif tile ==75:
                    slime=Jugador.jugador(image_x,image_y,animacion_mops[4],Constantes.vida_slime,2)
                    self.lista_mops.append(slime)
                    tile_data[0]=tile_list[17]
                #crear mop guardiareal esqueleto
                elif tile ==76:
                    guardia_real_esqueleto=Jugador.jugador(image_x,image_y,animacion_mops[2],Constantes.vida_guardia_real_esueleto,2)
                    self.lista_mops.append(guardia_real_esqueleto)
                    tile_data[0]=tile_list[29]
                #crear mop jefe piso    
                elif tile ==64:
                    jefe_de_piso=Jugador.jugador(image_x,image_y,animacion_mops[3],Constantes.vida_jefe,2)
                    self.lista_mops.append(jefe_de_piso)
                    tile_data[0]=tile_list[11]
                self.map_tiles.append(tile_data)
                
    
    def cambiar_puerta(self, jugador,tile_list ):
        buffer=Constantes.rango_para_abrir_puerta
        proximidad_rect=pygame.Rect(jugador.forma.x-buffer,jugador.forma.y-buffer,jugador.forma.width+2*buffer,jugador.forma.height+2*buffer)
        for tile_data in self.map_tiles:
            image,rect,x,y,tile_type=tile_data
            if proximidad_rect.colliderect(rect):
                if tile_type in puerta_cerrada:
                    if tile_type==36 or tile_type==66:
                        new_tile_type=57
                    elif tile_type== 37 or tile_type==67:
                        new_tile_type=58
                    elif tile_type== 38:
                        new_tile_type=39

                    tile_data[4]=new_tile_type
                    tile_data[0]=tile_list[new_tile_type]

                    #elimina el tile de la lita de coliciones
                    if tile_data in self.obstaculos_tiles:
                        self.obstaculos_tiles.remove(tile_data)

                    return True
        return False

    def update(self, posicion_pantalla):
        for tile in self.map_tiles:
            tile[2] +=posicion_pantalla[0]
            tile[3] +=posicion_pantalla[1]
            tile[1].center=(tile[2],tile[3])

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0],tile[1])