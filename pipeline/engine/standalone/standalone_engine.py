from pipeline.engine import engine
import subprocess, os, platform

class StandaloneEngine(engine.Engine):

    
    def open(self, path):
        if(platform.system() == "Windows"):
            os.startfile(path)
        pass

    def save(self):
        pass

    def export(self, in_file):

        mayabatch = "D:/Maya2020/Maya2020/bin/mayabatch.exe"
        abc_export_script = "D:/Artfx/GarciaTD4/Python-DCC/pipeline/abc/abc_export.py"
        out = "D:/Artfx/GarciaTD4/Python-DCC/export/"

        exec_file = "python(\"execfile(\'{}\')\");".format(abc_export_script)

        maya_export_query = [mayabatch, '-command', exec_file, in_file, out,"root model pSphere"]

        subprocess.call(maya_export_query, shell=True)

        pass

    def importation(self, directory):
        hython = "C:/Program Files/Side Effects Software/Houdini 18.0.566/bin/hython.exe"
        houdini_import = "D:/Artfx/GarciaTD4/Python-DCC/pipeline/engines/houdini/houdini_import.py"
   
        houdini_import_query = [hython, houdini_import, directory, directory]
        print(houdini_import_query)
        subprocess.call(houdini_import_query, shell=True)

        pass

