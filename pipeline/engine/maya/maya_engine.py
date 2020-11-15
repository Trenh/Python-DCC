import sys, os
from pipeline.engine import engine
import maya.cmds as cmds


class MayaEngine(engine.Engine):

    def open(self, path):
        cmds.file(new=True, force=True)
        cmds.file(path, open=True)
        pass

    def save(self):
        cmds.file(rename="D:/Artfx/GarciaTD4/Python-DCC/savedfile.ma")
        cmds.file(save=True, type="mayaAscii")
        pass