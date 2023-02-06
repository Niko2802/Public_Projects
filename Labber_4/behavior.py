from core_objects import GeomObject
import pygame

class ObstacleBehaviorBase():
    def __init__(self, isobstacle) -> None:
        self.isobstacle = isobstacle

    def is_obstacle(self):
        return self.isobstacle

class ObstacleBehavior(ObstacleBehaviorBase):
    def __init__(self, ctrl) -> None:
        super().__init__(True)


class NoObstacleBehavior(ObstacleBehaviorBase):
    def __init__(self, ctrl) -> None:
        super().__init__(False)


class FlipObstacleBehavior():
    def __init__(self, ctrl) -> None:
        self.ctrl = ctrl
    
    def is_obstacle(self):
        return not self.ctrl.status
    

class ControlBehavior():
    def __init__(self) -> None:
        self.status = False
    
    def interact(self):
        self.status = not self.status

class NoControlBehavior():
    def __init__(self) -> None:
        self.status = False

    def interact(self):
        pass

class RemoteTargetControl():
    def __init__(self) -> None:
        self.status = False

    def interact(self):
        pass

    def remote_interact(self):
        self.status = not self.status


class RemoteSourceControl():
    def __init__(self) -> None:
        self.obj = None
        self.status = False

    def interact(self):
        self.status = not self.status
        self.obj.control.remote_interact()

    def link(self, obj):
        self.obj = obj
        self.obj.bind_control(RemoteTargetControl())




class OneWayControl():
    def __init__(self) -> None:
        self.status = False
    
    def interact(self):
        self.status = True

class CoinBehavior():
    def __init__(self, ctrl) -> None:
        self.value = 4
        self.ctrl = ctrl
    def money(self):
        if not self.ctrl.status:
            self.ctrl.status = True
            return self.value
        return 0

class ChestBehavior():
    def __init__(self, ctrl) -> None:
        self.value = 50
        self.ctrl = ctrl
        self.is_take = False
    def money(self):
        if self.ctrl.status and not self.is_take:
            self.is_take=True
            return self.value
        return 0


class NoMoneyBehavior():
    def __init__(self, ctrl) -> None:
        pass
    def money(self):
        return 0


class SingleDrawBehavior():
    def __init__(self, imgs, ctrl) -> None:
        self.img = pygame.image.load(imgs[0])

    def draw(self, scr, x, y):
        scr.blit(self.img, (x, y))


class DoubleDrawBehavior():
    def __init__(self, imgs, ctrl) -> None:
        self.img1 = pygame.image.load(imgs[0])
        self.img2 = None
        if len(imgs) > 1:
            self.img2 = pygame.image.load(imgs[1])
        self.ctrl = ctrl

    def draw(self, scr, x, y):
        img = self.img2 if self.ctrl.status else self.img1
        if not img is None:
            scr.blit(img, (x, y))

