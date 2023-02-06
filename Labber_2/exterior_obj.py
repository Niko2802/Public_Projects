import pygame
from draw_objects import DrawObject, DoubleDrawObject
from core_objects import IInteract, IRemote, IMoney


class Hero(DrawObject):
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

    def is_obstacle(self):
        return True


class Coin(DoubleDrawObject, IMoney):
    img = pygame.image.load(r"Labber/img/coins.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Coin.img, None)
        self.value = 4

    def is_obstacle(self):
        return False

    def money(self):
        if not self.status:
            self.status = True
            return self.value
        return 0

class Wall(DrawObject):
    img=pygame.image.load(r"Labber/img/wall.png")
    def __init__(self, x, y) -> None:
        super().__init__(x, y, Wall.img)

    def is_obstacle(self):
        return True

class BaseGate(DoubleDrawObject, IInteract):
    img1 = pygame.image.load(r"Labber/img/gate_close.png")
    img2 = pygame.image.load(r"Labber/img/gate_open.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Gate.img1, Gate.img2)

    def is_obstacle(self):
        return not self.status

class Gate(BaseGate):
    def interact(self):
        self.status = not self.status

class SwitchedGate(BaseGate, IRemote):
    def interact(self):
        pass

    def remote_interact(self):
        self.status = not self.status


class Layer(DoubleDrawObject, IInteract):
    img1 = pygame.image.load(r"Labber/img/layer_off.png")
    img2 = pygame.image.load(r"Labber/img/layer_on.png")

    def __init__(self, x, y, obj: IRemote) -> None:
        super().__init__(x, y, Layer.img1, Layer.img2)
        self.obj=obj

    def is_obstacle(self):
        return True

    def interact(self):
        self.status = not self.status
        self.obj.remote_interact()


class Chest(DoubleDrawObject, IMoney, IInteract):
    img1=pygame.image.load(r"Labber/img/close_chest.png")
    img2=pygame.image.load(r"Labber/img/open_chest.png")

    def __init__(self, x, y) -> None:
        super().__init__(x, y, Chest.img1, Chest.img2)
        self._value=50
        self.is_take=False

    def interact(self):
        self.status=True

    def money(self):
        if self.status and not self.is_take:
            self.is_take=True
            return self._value
        return 0

    def is_obstacle(self):
        return False

