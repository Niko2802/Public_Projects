import pygame
from draw_objects import DrawObject, DoubleDrawObject
from core_objects import *


class Hero(DrawObject, Obstacle):
    img = pygame.image.load(r"Labber/img/olaf1.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Hero.img)
        self.money = 0

    def move(self, rect):
        self.x = rect.x
        self.y = rect.y

    def take_item(self, item):
        if isinstance(item, IMoney):
            self.money += item.money()


class Coin(DoubleDrawObject, NotObstacle, IMoney):
    img = pygame.image.load(r"Labber/img/coins.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Coin.img, None)
        self.value = 4

    def money(self):
        if not self.status:
            self.status = True
            return self.value
        return 0

class Wall(DrawObject, Obstacle):
    img=pygame.image.load(r"Labber/img/wall.png")
    def __init__(self, x, y) -> None:
        super().__init__(x, y, Wall.img)


class BaseGate(DoubleDrawObject, SwitchedObstacle):
    img1 = pygame.image.load(r"Labber/img/gate_close.png")
    img2 = pygame.image.load(r"Labber/img/gate_open.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Gate.img1, Gate.img2)


class Gate(BaseGate, FlipInteract):
    pass


class SwitchedGate(BaseGate):
    def remote_interact(self):
        self.status = not self.status


class Layer(DoubleDrawObject, Obstacle, RemoteInteract):
    img1 = pygame.image.load(r"Labber/img/layer_off.png")
    img2 = pygame.image.load(r"Labber/img/layer_on.png")

    def __init__(self, x, y, obj) -> None:
        super().__init__(x, y, Layer.img1, Layer.img2)
        self.obj=obj


class Chest(DoubleDrawObject, IMoney, OnlyOpenInteract, NotObstacle):
    img1=pygame.image.load(r"Labber/img/close_chest.png")
    img2=pygame.image.load(r"Labber/img/open_chest.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Chest.img1, Chest.img2)
        self._value=50
        self.is_take=False

    def money(self):
        if self.status and not self.is_take:
            self.is_take=True
            return self._value
        return 0

