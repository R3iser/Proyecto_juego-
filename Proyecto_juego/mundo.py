import Constantes
import items
import Jugador

obstaculos=[0,1,2,3,4,5,10,15,20,25,30,35,36,37,40,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,58,66,67,78]

class mundo():
    def __init__(self):
        self.map_tiles=[]
        self.obstaculos_tiles=[]
        self.exit_tile=None
        self.lista_item=[]
        self.lista_mops=[]

    def  process_data(self, data,tile_list,item_imagenes,animacion_mops):
        self.level_length =len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image=tile_list[tile]
                image_rect=image.get_rect()
                image_x=x*Constantes.tile_size
                image_y=y*Constantes.tile_size
                image_rect.center=(image_x, image_y)
                tile_data=[image,image_rect,image_x,image_y ]
                #tiles a obstaculos
                if tile in obstaculos:
                    self.obstaculos_tiles.append(tile_data)
                #tile salida
                elif tile == 39:
                    self.exit_tile=tile_data
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
                    esqueleto=Jugador.jugador(image_x,image_y,animacion_mops[1],100,2)
                    self.lista_mops.append(esqueleto)
                    tile_data[0]=tile_list[26]
                #crear mop esqueleto acorasado
                elif tile==77:
                    esqueleto_acorasado=Jugador.jugador(image_x,image_y,animacion_mops[0],200,2)
                    self.lista_mops.append(esqueleto_acorasado)
                    tile_data[0]=tile_list[28]
                self.map_tiles.append(tile_data)

    def update(self, posicion_pantalla):
        for tile in self.map_tiles:
            tile[2] +=posicion_pantalla[0]
            tile[3] +=posicion_pantalla[1]
            tile[1].center=(tile[2],tile[3])

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0],tile[1])