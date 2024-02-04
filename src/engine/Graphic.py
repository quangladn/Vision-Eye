from .Object import *
import pygame


class Graphic(Object):
    def __init__(self) -> None:
        super().__init__()
        self.x: int | float = 0
        self.y: int | float = 0
        self.color = (255, 255, 255)
        self.alpha = 255
        self.angle = 0

    def Update(self, world):
        self.Script(world, self)


class Polygon(Graphic):
    def __init__(self) -> None:
        super().__init__()
        self.Points = []
        self.maxWidth: int | float = 0
        self.maxHeight: int | float = 0

    def SetNewPoints(self, points):
        self.Points = points
        self.maxWidth, self.maxHeight = self.UpdateWithHeight()

    def UpdateWithHeight(self):
        maxX = 0
        maxY = 0
        for point in self.Points:
            x = point[0]
            y = point[1]
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
        return maxX, maxY

    def Render(self, Window):
        surface = pygame.Surface((self.maxWidth, self.maxHeight))
        pygame.draw.polygon(surface, self.color, self.Points)
        Window.display.blit(surface, (self.x, self.y))
        # print(123)
