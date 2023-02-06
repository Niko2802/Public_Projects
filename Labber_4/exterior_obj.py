import pygame
from core_objects import GeomObject
from behavior import *

class ObjectsFactory():
    control_factory = {
        "NoControl": NoControlBehavior,
        "Control": ControlBehavior,
        "OneWayControl": OneWayControl,
        "RemoteControl": RemoteSourceControl
    }
    obstacle_factory = {
        "Obstacle": ObstacleBehavior,
        "NoObstacle": NoObstacleBehavior,
        "FlipObstacle": FlipObstacleBehavior
    }
    draw_factory = {
        "Single": SingleDrawBehavior,
        "Double": DoubleDrawBehavior
    }
    money_factory = {
        "NoMoney": NoMoneyBehavior,
        "Coin": CoinBehavior,
        "Chest": ChestBehavior
    }
    
    @staticmethod
    def create(cls, *args):
        return [cls(x, y) for x, y in args]

    @staticmethod
    def create_from_json(key, val):
        control_name = val["control"]
        # control = ObjectsFactory.control_factory[control_name]()
        obstacle_name = val["obstacle"]
        # obstacle = ObjectsFactory.obstacle_factory[obstacle_name](control)
        draw_name = val["draw"]
        imgs = val["images"]
        # draw = ObjectsFactory.draw_factory[draw_name](imgs, control)
        money_name = val["money"]
        # money = 
        dst = val.get("dst")
        res = []
        for x, y in val["coords"]:
            obj = ExteriorObject(x, y)
            control = ObjectsFactory.control_factory[control_name]()
            obj.control = control
            obj.obs_behavior = ObjectsFactory.obstacle_factory[obstacle_name](control)
            obj.draw_behavior = ObjectsFactory.draw_factory[draw_name](imgs, control)
            obj.money_behavior = ObjectsFactory.money_factory[money_name](control)
            obj.dst = dst
            res.append(obj)
        return res


class Hero(GeomObject):
    img = ["Labber_4/img/olaf1.png"]

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.money = 0
        self.obs_behavior = ObstacleBehavior(True)
        self.draw_behavior = SingleDrawBehavior(Hero.img, None)

    def move(self, rect):
        self.x = rect.x
        self.y = rect.y

    def take_item(self, item):
        self.money += item.money()

    def is_obstacle(self):
        return self.obs_behavior.is_obstacle()

    def draw(self, scr):
        self.draw_behavior.draw(scr, self.x, self.y)


class ExteriorObject(GeomObject):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.obs_behavior = None
        self.draw_behavior = None
        self.money_behavior = None
        self.dst = None

    def is_obstacle(self):
        return self.obs_behavior.is_obstacle()

    def draw(self, scr):
        self.draw_behavior.draw(scr, self.x, self.y)

    def interact(self):
        self.control.interact()
    
    def money(self):
        return self.money_behavior.money()
    
    def bind_control(self, control):
        self.control = control
        self.obs_behavior.ctrl = control
        self.draw_behavior.ctrl = control
        self.money_behavior.ctrl = control
    
    def link(self, obj):
        self.control.link(obj)




# class Wall(GeomObject):
#     img=pygame.image.load(r"Labber/img/wall.png")
#     def __init__(self, x, y) -> None:
#         super().__init__(x, y)
#         self.draw_behavior = SingleDrawBehavior(Wall.img)
#         self.obs_behavior = ObstacleBehavior(True)
#         self.control = NoControlBehavior()
#         self.money_behavior = NoMoneyBehavior(self.control)

#     def is_obstacle(self):
#         return self.obs_behavior.is_obstacle()
    
#     def interact(self):
#         self.control.interact()

#     def money(self):
#         return self.money_behavior.money()
    
#     def draw(self, scr):
#         self.draw_behavior.draw(scr, self.x, self.y)


# class Coin(GeomObject, IMoney):
#     img = pygame.image.load(r"Labber/img/coins.png")

#     def __init__(self, x, y) -> None:
#         super().__init__(x, y)
#         self.obs_behavior = ObstacleBehavior(False)
#         self.control = NoControlBehavior()
#         self.draw_behavior = DoubleDrawBehavior(Coin.img, None, self.control)
#         self.money_behavior = CoinBehavior(self.control)

#     def is_obstacle(self):
#         return self.obs_behavior.is_obstacle()

#     def money(self):
#         return self.money_behavior.money()

#     def interact(self):
#         self.control.interact()

#     def draw(self, scr):
#         self.draw_behavior.draw(scr, self.x, self.y)


# class Chest(GeomObject, IMoney, IInteract):
#     img1=pygame.image.load(r"Labber/img/close_chest.png")
#     img2=pygame.image.load(r"Labber/img/open_chest.png")

#     def __init__(self, x, y) -> None:
#         super().__init__(x, y)
#         self.is_take=False
#         self.control = OneWayControl()
#         self.obs_behavior = ObstacleBehavior(False)
#         self.draw_behavior = DoubleDrawBehavior(Chest.img1, Chest.img2, self.control)
#         self.money_behavior = ChestBehavior(self.control)

#     def interact(self):
#         self.control.interact()

#     def draw(self, scr):
#         self.draw_behavior.draw(scr, self.x, self.y)

#     def money(self):
#         return self.money_behavior.money()

#     def is_obstacle(self):
#         return self.obs_behavior.is_obstacle()


# class Gate(GeomObject, IInteract):
#     img1 = pygame.image.load(r"Labber/img/gate_close.png")
#     img2 = pygame.image.load(r"Labber/img/gate_open.png")

#     def __init__(self, x, y) -> None:
#         super().__init__(x, y)
#         self.bind_control(ControlBehavior())
#     def is_obstacle(self):
#         return self.obs_behavior.is_obstacle()

#     def draw(self, scr):
#         self.draw_behavior.draw(scr, self.x, self.y)

#     def interact(self):
#         self.control.interact()
    
#     def money(self):
#         return self.money_behavior.money()
    
#     def bind_control(self, control):
#         self.control = control
#         self.obs_behavior = FlipObstacleBehavior(self.control)
#         self.draw_behavior = DoubleDrawBehavior(Gate.img1, Gate.img2, self.control)
#         self.money_behavior = NoMoneyBehavior(self.control)


# class Layer(GeomObject, IInteract):
#     img1 = pygame.image.load(r"Labber/img/layer_off.png")
#     img2 = pygame.image.load(r"Labber/img/layer_on.png")

#     def __init__(self, x, y, obj: IRemote) -> None:
#         super().__init__(x, y)
#         self.control = RemoteSourceControl(obj)
#         self.draw_behavior = DoubleDrawBehavior(Layer.img1, Layer.img2, self.control)
#         self.obs_behavior = ObstacleBehavior(True)
#         self.money_behavior = NoMoneyBehavior(self.control)

#     def is_obstacle(self):
#         return self.obs_behavior.is_obstacle()

#     def interact(self):
#         self.control.interact()
    
#     def money(self):
#         return self.money_behavior.money()

#     def draw(self, scr):
#         self.draw_behavior.draw(scr, self.x, self.y)

class Stub():
    def is_obstacle(self):
        return False
    def interact(self):
        pass
    def money(self):
        return 0
