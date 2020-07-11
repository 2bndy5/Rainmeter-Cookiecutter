import os
import shutil
import configparser
from subprocess import run

import_type = "{{ cookiecutter.import_type }}"
importing = "{{ cookiecutter.import }}"
rm_skins_path = r"{{ cookiecutter._skins_path }}"
rm_layouts_path = r"{{ cookiecutter._layouts_path }}"
init_commit = "{{ cookiecutter._init_commit }}"
init_commit = False if init_commit == "False" else True

def remove_blank_skin():
    for dirpath, dirnames, filenames in os.walk(
        os.getcwd() + os.sep + "Skins", topdown=False
    ):
        for f in filenames:
            os.remove(dirpath + os.sep + f)
        for d in dirnames:
            os.rmdir(dirpath + os.sep + d)


def import_skin(root_config):
    print(f"importing {root_config} skin")
    new_dir = "Skins" + os.sep + root_config
    skin_root = rm_skins_path + os.sep + root_config
    shutil.copytree(skin_root, new_dir)


def read_config(file_path):
    parser = configparser.ConfigParser(default_section="Rainmeter")
    try:  # trys to open file with default utf-8 encoding
        parser.read(file_path)
    except configparser.MissingSectionHeaderError:
        # This exception on this file likely means encoding is utf-16
        parser.read(file_path, encoding="utf-16")
    finally:
        return parser


def gather_layout_deps(layout_name):
    parsed = read_config(
        rm_layouts_path + os.sep + layout_name + os.sep + "Rainmeter.ini"
    )
    needed_skins = []
    for key in parsed.keys():
        # exclude inactive skins & [Rainmeter] section
        if "Active" in parsed[key] and bool(int(parsed[key]["Active"])):
            # only grab root config name as a necessary skin for layout
            root_config = key.split(os.sep)[0]
            if not root_config in needed_skins:
                # avoid duplicate entries
                needed_skins.append(root_config)
    return needed_skins


if import_type == "Skin":
    # ``importing`` is a str
    if importing != "Create a new skin":
        remove_blank_skin()
        import_skin(importing)
elif import_type == "Layout":
    # ``importing`` is a list
    remove_blank_skin()
    # needed_skins =
    for name in gather_layout_deps(importing):
        import_skin(name)
    # copy layout file
    print(f"importing {importing} layout")
    dst = "Layouts" + os.sep + importing
    os.mkdir("Layouts")
    os.mkdir(dst)
    src = rm_layouts_path + os.sep + importing + os.sep + "Rainmeter.ini"
    shutil.copy2(src, dst)

if init_commit:
    run(["git", "init"])
    try:
        # sometimes ``git init`` generates a blank README.md
        os.remove("README.md")
    except FileNotFoundError:
        # sometimes not
        pass
    run(["git", "add", "."])
    run(["git", "commit", "-m", "Initial commit"])