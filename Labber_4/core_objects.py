import pygame, abc



class IObstacle(abc.ABC):
    @abc.abstractmethod
    def is_obstacle(self):
        pass

class IDraw(abc.ABC):
    @abc.abstractmethod
    def draw(self, scr):
        pass

class IInteract(abc.ABC):
    @abc.abstractmethod
    def interact(self):
        pass

class IRemote(abc.ABC):
    @abc.abstractmethod
    def remote_interact(self):
        pass

class IMoney(abc.ABC):
    @abc.abstractmethod
    def money(self):
        pass



class GeomObject(IObstacle):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_rect(self, x=0, y=0):
        return pygame.Rect(self.x+x, self.y+y, 50 , 50)

    def collide(self, rect):
        return self.get_rect().colliderect(rect)


