from pipeline.engine import engine
import hou 


class HoudiniEngine(engine.Engine):

    def open(self, path):
        hou.hipFile.load(path)
        pass

    def save(self):
        print("houdini engine save")
        hou.hipFile.save(r"D:\Artfx\GarciaTD4\Python-DCC\saved.hip")
        pass
    