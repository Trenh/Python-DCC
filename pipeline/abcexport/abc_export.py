import sys, os
import maya.cmds as cmds

cmds.loadPlugin( 'AbcExport.mll' )
cmds.loadPlugin( 'AbcImport.mll' )
print('Start abc export')

in_file = sys.argv[3]
directory_out = sys.argv[4]
cmds.file(new=True, force=True)
cmds.file(in_file, open=True)


selected_namespace = "model"

# Get all the object from the scene with the input namespace
namespace = "{}:*".format(selected_namespace)
trans_obj = cmds.ls(namespace, type='transform')

for abc_obj in trans_obj:
    print(abc_obj.split(':')[1])
    namefile = abc_obj.split(':')[1]
    command ="-frameRange 1 120 -uvWrite -dataFormat ogawa -root {0} -file {1}{2}.abc".format(abc_obj, directory_out, namefile)
    print("commande  " + command)
    cmds.AbcExport(j=command, verbose=True)


print("finished export")