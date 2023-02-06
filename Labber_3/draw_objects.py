import pygame
from core_objects import GeomObject

class DrawObject(GeomObject):
    def __init__(self, x, y, img) -> None:
        super().__init__(x, y)
        self.img = img

    def draw(self, scr):
        scr.blit(self.img, (self.x, self.y))


class DoubleDrawObject(GeomObject):
    def __init__(self, x, y, img1, img2) -> None:
        super().__init__(x, y)
        self.img1 = img1
        self.img2 = img2
        self.status = False

    def draw(self, scr):
        img = self.img2 if self.status else self.img1
        if not img is None:
            scr.blit(img, (self.x, self.y))

    # def collide(self, rect):
    #     if self.status:
    #         return False
    #     return super().collide(rect)

    # def interact(self):
    #     self.status = not self.status

