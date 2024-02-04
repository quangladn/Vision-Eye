from .Constance import *


class Object:
    def __init__(self) -> None:
        self.Enable = True
        self.Script = NoneFunction
        self.UpdateData = []

    def SetScript(self, script):
        self.Script = script
