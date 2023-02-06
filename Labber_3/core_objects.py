import pygame, abc


class BaseObjects():
    @classmethod
    def create(cls, *args):
        return [cls(x, y) for x, y in args]

class IObstacle(abc.ABC):
    @abc.abstractmethod
    def is_obstacle(self):
        pass

# class IDraw(abc.ABC):
#     @abc.abstractmethod
#     def draw(self, scr):
#         pass

class IInteract(abc.ABC):
    @abc.abstractmethod
    def interact(self):
        pass

# class IRemote(abc.ABC):
#     @abc.abstractmethod
#     def remote_interact(self):
#         pass

class IMoney(abc.ABC):
    @abc.abstractmethod
    def money(self):
        pass

class NotObstacle(IObstacle):
    def is_obstacle(self):
        return False

class Obstacle(IObstacle):
    def is_obstacle(self):
        return True

class SwitchedObstacle(IObstacle):
    def is_obstacle(self):
        return not self.status

class FlipInteract(IInteract):
    def interact(self):
        self.status = not self.status

class RemoteInteract(IInteract):
    def interact(self):
        self.status = not self.status
        self.obj.remote_interact()

class OnlyOpenInteract(IInteract):
    def interact(self):
        self.status=True



class GeomObject(BaseObjects):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_rect(self, x=0, y=0):
        return pygame.Rect(self.x+x, self.y+y, 50 , 50)

    def collide(self, rect):
        return self.get_rect().colliderect(rect)


class Stub():
    def is_obstacle(self):
        return False
    def interact(self):
        return 0
