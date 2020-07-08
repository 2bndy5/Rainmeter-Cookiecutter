import os
import shutil

imported_skin = "{{ cookiecutter.import_skin }}"
rm_skins_path = r"{{ cookiecutter._skins_path }}"
if imported_skin != "Create a new skin":
    for dirpath, dirnames, filenames in os.walk(os.getcwd() + os.sep + "Skins", topdown=False):
        for f in filenames:
            os.remove(dirpath + os.sep + f)
        for d in dirnames:
            os.rmdir(dirpath + os.sep + d)
    
    print("importing", imported_skin)
    new_dir = "Skins" + os.sep + imported_skin
    skin_root = rm_skins_path + os.sep + imported_skin
    shutil.copytree(skin_root, new_dir)