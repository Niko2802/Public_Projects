import pygame


class BaseObjects():
    @classmethod
    def create(cls, *args):
        return [cls(x, y) for x, y in args]

class GeomObject(BaseObjects):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_rect(self, x=0, y=0):
        return pygame.Rect(self.x+x, self.y+y, 50 , 50)

    def collide(self, rect):
        return self.get_rect().colliderect(rect)


