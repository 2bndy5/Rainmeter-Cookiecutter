"""
This script will probe your system for rainmeter info to fill in the
default variables used in the cookiecutter process.
"""
import os
import time
import winreg
import configparser
import json
from cookiecutter.main import cookiecutter
from cookiecutter import prompt

defaults = {
    "author_full_name": os.getenv("USERNAME"),
    "github_username": "my.github.account",
    "req_rainmeter_version": "4.3",
    "_year": time.strftime("%Y", time.localtime()),
    "_skins_path": "",
    "_layouts_path": "",
    "installed": {"Skin": ["Create a new skin"], "Layout": []},
    "import_type": ["Skin", "Layout"],
    "import": [],
    "_load_skin": "NONE",
    "project_name": "",
    "repository_name": "",
    "short_description": "A collection of my skins for Rainmeter",
    "license": ["MIT", "CC BY-SA", "GNU GPLv3"],
    "_copy_without_render": ["*.github/*"],
}


def list_to_string(data, indent=0):
    result = ""
    for item in data:
        if isinstance(item, dict):
            result += dict_to_str(item, indent + 1)
        elif isinstance(item, list):
            if len(item) > 1:
                result += list_to_string(item, indent + 1)
            else:
                result += " " * 2 * indent + '- "' + item[0] + '"\n'
        else:
            result += " " * 2 * indent + '- "' + item + '"\n'
    return result


def dict_to_str(data, indent=0):
    result = ""
    for k, v in data.items():
        if isinstance(v, dict):
            result += " " * 2 * indent + k.replace(" ", "_") + ":\n"
            result += dict_to_str(v, indent + 1)
        elif isinstance(v, list):
            result += " " * 2 * indent + k.replace(" ", "_") + ":\n"
            result += list_to_string(v, indent + 1)
        else:
            result += " " * 2 * indent + k.replace(" ", "_") + ': "' + v + '"\n'
    return result


def dump_to_yml(data_dict, filename):
    with open(filename + ".yml", "w") as file:
        file.write(dict_to_str(data_dict))


def read_config(file_path):
    parser = configparser.ConfigParser(default_section="Rainmeter")
    try:  # trys to open file with default utf-8 encoding
        parser.read(file_path)
    except configparser.MissingSectionHeaderError:
        # This exception on this file likely means encoding is utf-16
        parser.read(file_path, encoding="utf-16")
    finally:
        return parser


def main():
    """Gathers default data before prompting user for input."""
    rm_reg_key = None
    try:
        rm_reg_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Rainmeter",
        )
    except FileNotFoundError:
        print("Rainmeter is not installed!")
    if rm_reg_key is not None:
        defaults["req_rainmeter_version"] = winreg.QueryValueEx(
            rm_reg_key, "DisplayVersion"
        )[0].replace(" r", ".")
        defaults["_layouts_path"] = (
            os.getenv("APPDATA") + os.sep + "Rainmeter\\Layouts"
        )

        # get path to Rainmeter skins
        parsed = read_config(os.getenv("APPDATA") + "\\Rainmeter\\Rainmeter.ini")
        if "Rainmeter" in parsed and "SkinPath" in parsed["Rainmeter"]:
            if parsed["Rainmeter"]["SkinPath"].endswith(os.sep):
                # remove trailing path seperator
                defaults["_skins_path"] = parsed["Rainmeter"][
                    "SkinPath"
                ][:-1]
            else:
                defaults["_skins_path"] = parsed["Rainmeter"][
                    "SkinPath"
                ]

        # grab names of installed skins
        if len(defaults["_skins_path"]):
            for d in os.listdir(defaults["_skins_path"]):
                if not d.startswith("@"):
                    # ignore @Backup & @Vault folders
                    defaults["installed"]["Skin"].append(d)

        # now collect layouts
        for d in os.listdir(defaults["_layouts_path"]):
            defaults["installed"]["Layout"].append(d)

    # Prompt user for input
    for key, value in defaults.items():
        if not key.startswith("_"):
            if isinstance(value, list):
                defaults[key] = prompt.read_user_choice(key, value)
            elif isinstance(value, str):
                defaults[key] = prompt.read_user_variable(key, value)
            if key.endswith("import_type"):
                defaults["import"] = defaults[
                    "installed"
                ][defaults[key]]
            elif key.endswith("import"):
                defaults["project_name"] = defaults[key]
                defaults["repository_name"] = (
                    defaults[key].replace(" ", "_")
                    + "_Rainmeter_Skin"
                )
                # promt user to pick skin to load if importing an installed skin
                if defaults["import_type"] == "Skin" and defaults["import"] != "Create a new skin":
                    # now ask the user which skin to load on-install
                    skin_configs = []
                    for dirpath, _, filenames in os.walk(
                        defaults["_skins_path"]
                        + os.sep
                        + defaults[key]
                    ):
                        for f in filenames:
                            if f.endswith(".ini"):
                                skin_configs.append(
                                    dirpath.replace(
                                        defaults["_skins_path"]
                                        + os.sep,
                                        "",
                                    )
                                    + os.sep
                                    + f
                                )
                    defaults["_load_skin"] = prompt.read_user_choice(
                        "skin to load", skin_configs
                    )
            elif key.endswith("project_name"):
                defaults["repository_name"] = (
                    defaults[key].replace(" ", "_")
                    + "_Rainmeter_Skin"
                )
                

    # NOTE debugging output functions
    # dump to JSON
    with open("defaults.json", "w") as file:
        json.dump(defaults, file, indent=4)


if __name__ == "__main__":
    main()
    # now merge discovered defaults and begin cookie-cutting
    cookiecutter(".", output_dir="..", extra_context=defaults, no_input=True)

