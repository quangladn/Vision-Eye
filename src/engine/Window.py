import pygame, time, threading
from .Object import *
from .Constance import *
from .KeyEvent import *


class Window(Object):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.display = pygame.display.set_mode(
            (720, 480), pygame.SCALED | pygame.RESIZABLE | pygame.SRCALPHA
        )

        self.backgroundColor = (0, 0, 0)

        # Time
        self.Timer = pygame.time.Clock()
        self.Millisecond = 0  # ms
        self.Second = 0  # s
        self.Fps = 60

        # Render
        self.Graphics = []

        # Event
        self.KeyDown = []

        threading.Thread(target=self.MsCounter).start()

    def AddGraphic(self, Graphic):
        self.Graphics.append(Graphic)

    def Render(self):
        self.display.fill(self.backgroundColor)
        for graphic in self.Graphics:
            graphic.Render(self)
        pygame.display.flip()

    def Input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Exit()
            elif event.type == pygame.KEYDOWN:
                self.KeyDown.append(event.key)
            elif event.type == pygame.KEYUP:
                self.KeyDown.remove(event.key)

    def UpdateGraphic(self):
        for graphic in self.Graphics:
            graphic.Update(self)

    def IsPressing(self, key):
        if key in self.KeyDown:
            return True
        return False

    def Run(self):
        while self.Enable:
            self.Input()
            # Update
            self.Script(self)
            self.UpdateGraphic()
            self.Render()
            # Set Fps
            self.Timer.tick(self.Fps)

    def Exit(self):
        self.Enable = False
        pygame.quit()
        exit(0)

    def MsCounter(self):
        while self.Enable:
            time.sleep(0.001)
            self.Millisecond += 2.5
            if self.Millisecond / 1000 >= 1:
                # print("End",end="\n")
                self.Millisecond = 0
                self.Second += 1 
            # else:
                # print("sec: "+str((self.Tick/1000)),end="\r")
            # self.Tick = 0
