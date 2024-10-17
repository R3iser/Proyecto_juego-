import Constantes

obstaculos=[0,1,2,3,4,5,10,15,20,25,30,35,40,41,42,43,44,45,50,51,52,53,54,55,]

class mundo():
    def __init__(self):
        self.map_tiles=[]
        self.obstaculos_tiles=[]
        self.exit=None

    def  process_data(self, data,tile_list):
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
                self.map_tiles.append(tile_data)

    def update(self, posicion_pantalla):
        for tile in self.map_tiles:
            tile[2] +=posicion_pantalla[0]
            tile[3] +=posicion_pantalla[1]
            tile[1].center=(tile[2],tile[3])

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0],tile[1])