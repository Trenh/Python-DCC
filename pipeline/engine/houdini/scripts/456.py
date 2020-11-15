import sys, os
import hou
print('Starting Houdini pipeline')

here = hou.getenv('HOUDINI_SCRIPT_PATH').split(';') [-1]
deployment_root = here.split('/pipeline/')[0]

print('Script root {}'.format(deployment_root))

sys.path.append(deployment_root)
sys.path.append(r'D:\Artfx\GarciaTD4\Python-DCC\lib')

print('Done Pipeline Config')