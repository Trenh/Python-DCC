import sys 

class Engine(object):

    def open(self, path):
        pass

    def save(self):
        pass

    def export(self, in_file):
        pass

    def importation(self, directory):
        pass


def get_current():

    engine = Engine()

    if 'maya' in sys.executable:
        from pipeline.engine.maya import maya_engine
        engine = maya_engine.MayaEngine()
        return engine

    if 'houdini' in sys.executable:
        from pipeline.engine.houdini import houdini_engine
        engine = houdini_engine.HoudiniEngine()
        return engine

    
    from pipeline.engine.standalone import standalone_engine
    engine = standalone_engine.StandaloneEngine()
    return engine

    