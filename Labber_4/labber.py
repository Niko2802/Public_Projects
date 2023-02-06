import pygame
import json
import exterior_obj as eo
from exterior_obj import ObjectsFactory



class Level():
    def __init__(self) -> None:
        # with open("Labber/level.json", "r") as f:
        #     lev = json.load(f)
        self.items = []
        self.hero=eo.Hero(50, 50)
        # walls=ObjectsFactory.create(eo.Wall, 
        #     (0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (
        #         400, 0), (450, 0), (500, 0), (550, 0), (600, 0), (650, 0), (700, 0), (750, 0),
        #     (0, 50),                                                                                                                                                                (750, 50),
        #     (0, 100), (50, 100), (100, 100), (150, 100), (200, 100), (250, 100), (300, 100), (350,
        #                                                                                       100), (400, 100), (450, 100), (500, 100), (550, 100), (600, 100), (650, 100),       (750, 100),
        #     (0, 150),                                                                                                                                                                        (750, 150),
        #     (0, 200), (50, 200), (100, 200), (150, 200), (200, 200), (250, 200), (300, 200), (350,
        #                                                                                       200),            (450, 200), (500, 200), (550, 200), (600, 200), (650, 200), (700, 200), (750, 200),
        #     (0, 250),                                                                                                                                                                        (750, 250),
        #     (0, 300), (50, 300), (100, 300), (150, 300), (200, 300), (250, 300), (300, 300), (350,
        #                                                                                       300), (400, 300), (450, 300), (500, 300), (550, 300),        (650, 300), (700, 300), (750, 300),
        #     (0, 350),                                                                                                                                                                        (750, 350),
        #     (0, 400), (50, 400),          (150, 400), (200, 400), (250, 400), (300, 400), (350, 400), (400,
        #                                                                                                400), (450, 400), (500, 400), (550, 400), (600, 400), (650, 400), (700, 400), (750, 400),
        #     (0, 450),                                                                                                                                                                     (750, 450),
        #     (0, 500), (50, 500), (100, 500), (150, 500), (200, 500), (250, 500), (300, 500), (350, 500), (400, 500), (450, 500), (500, 500), (550, 500), (600, 500), (650, 500), (700, 500), (750,
        #                                                                                                                                                                                       500),                                                                                                                                                                       (750, 500),
        # )
        # coins=ObjectsFactory.create(eo.Coin, 
        #     (100, 50), (300, 50), (400, 50),
        #     (250, 150), (600, 150),
        #     (150, 250), (450, 250), (700, 250),
        # )
        # gates=ObjectsFactory.create(eo.Gate, (250, 50))
        # chests=ObjectsFactory.create(eo.Chest, (150, 50), (50, 350), (700, 450))
        # sg=eo.Gate(400, 200)
        # layer=eo.Layer(50, 150, sg)
        # self.__add(walls, coins, gates, sg, chests, layer, self.hero)
    
    @staticmethod
    def create(name):
        with open(f"Labber_4/{name}.json", "r") as f:
            level_data = json.load(f)
        level = Level()
        for key in level_data:
            level.__add(ObjectsFactory.create_from_json(key, level_data[key]))
        level.link()
        return level

    
    def __add(self, *args):
        for x in args:
            if isinstance(x, list):
                self.items.extend(x)
            else:
                self.items.append(x)
    
    def __get(self, rect):
        for item in self.items:
            if item.get_rect() == rect:
                return item
        return eo.Stub()


    def draw(self, scr):
        scr.fill((0, 0, 0))
        f=font.render(f"Score: {self.hero.money}", True, (210, 210, 210))
        scr.blit(f, (50, 560))
        for item in self.items:
            item.draw(scr)
        self.hero.draw(scr)

    def key_handler(self, key):
        x=y=0
        if key == pygame.K_SPACE:
            self.interact()
            return
        if key == pygame.K_UP:
            y -= 50
        if key == pygame.K_DOWN:
            y += 50
        if key == pygame.K_LEFT:
            x -= 50
        if key == pygame.K_RIGHT:
            x += 50
        self.collide(x, y)

    def collide(self, x, y):
        hero_rect=self.hero.get_rect(x, y)
        obj=self.__get(hero_rect)
        if not obj.is_obstacle():
            self.hero.move(hero_rect)
            self.hero.take_item(obj)

    def interact(self):
        def internal_interact(x, y):
            hero_rect=self.hero.get_rect(x, y)
            obj=self.__get(hero_rect)
            if obj is not None:
                obj.interact()
                self.hero.take_item(obj)
        internal_interact(0, -50)
        internal_interact(50, 0)
        internal_interact(0, 50)
        internal_interact(-50, 0)

    def link(self):
        srcs = [x for x in self.items if x.dst is not None]
        for o in srcs:
            dst = self.__get(pygame.Rect(o.dst[0], o.dst[1], 50 , 50))
            o.link(dst)


pygame.init()
scr=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Labber")
clock=pygame.time.Clock()
fps=30
is_running=True
font=pygame.font.SysFont("Arial", 16)

level=Level.create("level")
 
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running=False
        if event.type == pygame.KEYDOWN:
            level.key_handler(event.key)

    level.draw(scr)
    clock.tick(fps)
    pygame.display.update()

pygame.quit()


# В exterior добавить метод линк и поле таргет, у лейра координаты у остальных нан
# Сделать так чтобы в RemoteControlBehavior объект передавался не в конструкторе
# Сделать линковку в левеле (связать лейр и гейт)
