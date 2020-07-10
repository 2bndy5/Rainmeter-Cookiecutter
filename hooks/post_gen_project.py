import os
import shutil

importing = "{{ cookiecutter.import }}"
rm_skins_path = r"{{ cookiecutter._skins_path }}"
rm_layouts_path = r"{{ cookiecutter._layouts_path }}"
import_type = "{{ cookiecutter.import_type }}"

def remove_blank_skin():
    for dirpath, dirnames, filenames in os.walk(os.getcwd() + os.sep + "Skins", topdown=False):
        for f in filenames:
            os.remove(dirpath + os.sep + f)
        for d in dirnames:
            os.rmdir(dirpath + os.sep + d)
    
def import_skin(root_config):
    print("importing", root_config)
    new_dir = "Skins" + os.sep + root_config
    skin_root = rm_skins_path + os.sep + root_config
    shutil.copytree(skin_root, new_dir)

if import_type == 'Skin':
    # ``importing`` is a str
    if importing != "Create a new skin":
        remove_blank_skin()
        import_skin(importing)
elif import_type == 'Layout':
    # ``importing`` is a list
    remove_blank_skin()
    for name in importing:
        import_skin(name)
