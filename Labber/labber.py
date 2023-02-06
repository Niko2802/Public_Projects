import pygame, json
from draw_objects import DoubleDrawObject, DrawObject
from core_objects import GeomObject


class Hero(DrawObject):
    img = pygame.image.load(r"Labber/img/olaf1.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Hero.img)
        self.money = 0

    def move(self, rect):
        self.x = rect.x
        self.y = rect.y

    def take_money(self, money):
        self.money += money

    def take_item(self, item):
        if isinstance(item, Coin):
            self.money += item.value
        if isinstance(item, Chest):
            self.money += item.value


class Coin(DrawObject):
    img = pygame.image.load(r"Labber/img/coins.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Coin.img)
        self.value = 4


class Gate(DoubleDrawObject):
    img1 = pygame.image.load(r"Labber/img/gate_close.png")
    img2 = pygame.image.load(r"Labber/img/gate_open.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Gate.img1, Gate.img2)


class SwitchedGate(Gate):
    def interact(self):
        self.status = False

    def remote_open(self):
        self.status = not self.status


class Layer(DoubleDrawObject):
    img1 = pygame.image.load(r"Labber/img/layer_off.png")
    img2 = pygame.image.load(r"Labber/img/layer_on.png")

    def __init__(self, x, y, obj) -> None:
        super().__init__(x, y, Layer.img1, Layer.img2)
        self.obj=obj

    def collide(self, rect):
        return GeomObject.collide(self, rect)

    def interact(self):
        super().interact()
        self.obj.remote_open()


class Chest(DoubleDrawObject):
    img1=pygame.image.load(r"Labber/img/close_chest.png")
    img2=pygame.image.load(r"Labber/img/open_chest.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Chest.img1, Chest.img2)
        self._value=50
        self.is_take=False

    def interact(self):
        self.status=True

    @ property
    def value(self):
        if not self.is_take:
            self.is_take=True
            return self._value
        return 0

    def collide(self, rect):
        return False


class ObjectCollection():
    def __init__(self) -> None:
        self.items=[]

    def draw(self, scr):
        for item in self.items:
            item.draw(scr)

    def collide(self, rect):
        for item in self.items:
            if item.collide(rect):
                return True
        return False

    def add(self, *args):
        for x in args:
            if isinstance(x, list):
                self.items.extend(x)
            else:
                self.items.append(x)

    def remove(self, item):
        if item is not None:
            self.items.remove(item)

    def get(self, rect):
        for item in self.items:
            if item.x == rect.x and item.y == rect.y:
                return item
        return None


class Wall(DrawObject):
    # image_name = r"Labber/img/wall.png"
    img=pygame.image.load(r"Labber/img/wall.png")
    def __init__(self, x, y) -> None:
        super().__init__(x, y, Wall.img)

# class Wall(DrawObject):
#     img = None
#     def __init__(self, x, y) -> None:
#         if Wall.img is None:
#             Wall.img = pygame.image.load(r"Labber/img/wall.png")
#         super().__init__(x, y, Wall.img)



class Level():
    def __init__(self) -> None:
        # with open("Labber/level.json", "r") as f:
        #     lev = json.load(f)
        self.hero=Hero(50, 50)
        walls=Wall.create(
            (0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (
                400, 0), (450, 0), (500, 0), (550, 0), (600, 0), (650, 0), (700, 0), (750, 0),
            (0, 50),                                                                                                                                                                (750, 50),
            (0, 100), (50, 100), (100, 100), (150, 100), (200, 100), (250, 100), (300, 100), (350,
                                                                                              100), (400, 100), (450, 100), (500, 100), (550, 100), (600, 100), (650, 100),       (750, 100),
            (0, 150),                                                                                                                                                                        (750, 150),
            (0, 200), (50, 200), (100, 200), (150, 200), (200, 200), (250, 200), (300, 200), (350,
                                                                                              200),            (450, 200), (500, 200), (550, 200), (600, 200), (650, 200), (700, 200), (750, 200),
            (0, 250),                                                                                                                                                                        (750, 250),
            (0, 300), (50, 300), (100, 300), (150, 300), (200, 300), (250, 300), (300, 300), (350,
                                                                                              300), (400, 300), (450, 300), (500, 300), (550, 300),        (650, 300), (700, 300), (750, 300),
            (0, 350),                                                                                                                                                                        (750, 350),
            (0, 400), (50, 400),          (150, 400), (200, 400), (250, 400), (300, 400), (350, 400), (400,
                                                                                                       400), (450, 400), (500, 400), (550, 400), (600, 400), (650, 400), (700, 400), (750, 400),
            (0, 450),                                                                                                                                                                     (750, 450),
            (0, 500), (50, 500), (100, 500), (150, 500), (200, 500), (250, 500), (300, 500), (350, 500), (400, 500), (450, 500), (500, 500), (550, 500), (600, 500), (650, 500), (700, 500), (750,
                                                                                                                                                                                              500),                                                                                                                                                                       (750, 500),
        )
        coins=Coin.create(
            (100, 50), (300, 50), (400, 50),
            (250, 150), (600, 150),
            (150, 250), (450, 250), (700, 250),
        )
        gates=Gate.create((250, 50))
        chests=Chest.create((150, 50), (50, 350), (700, 450))
        sg=SwitchedGate(400, 200)
        layer=Layer(50, 150, sg)

        self.obstacles=ObjectCollection()
        self.obstacles.add(walls, layer, gates, sg)
        self.pick_ups=ObjectCollection()
        self.pick_ups.add(coins)
        self.interacts=ObjectCollection()
        self.interacts.add(gates, sg, chests, layer)
        self.drawes=ObjectCollection()
        self.drawes.add(walls, coins, gates, sg, chests, layer, self.hero)

    def draw(self, scr):
        scr.fill((0, 0, 0))
        f=font.render(f"Score: {self.hero.money}", True, (210, 210, 210))
        scr.blit(f, (50, 560))
        self.drawes.draw(scr)

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
        collide=self.obstacles.collide(hero_rect)
        if not collide:
            self.hero.move(hero_rect)
        collide_pick_up=self.pick_ups.collide(hero_rect)
        if collide_pick_up:
            pick_up=self.pick_ups.get(hero_rect)
            self.pick_ups.remove(pick_up)
            self.drawes.remove(pick_up)
            self.hero.take_item(pick_up)

    def interact(self):
        def internal_interact(x, y):
            hero_rect=self.hero.get_rect(x, y)
            obj=self.interacts.get(hero_rect)
            if obj is not None:
                obj.interact()
                self.hero.take_item(obj)
        internal_interact(0, -50)
        internal_interact(50, 0)
        internal_interact(0, 50)
        internal_interact(-50, 0)


pygame.init()
scr=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Labber")
clock=pygame.time.Clock()
fps=30
is_running=True
font=pygame.font.SysFont("Arial", 16)

level=Level()

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


# Разобраться в коде. Создать ворота, которые будут открываться переключателем.
