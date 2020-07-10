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

defaults = {
    "req_rainmeter_version": "4.3",
    "author_full_name": os.getenv("USERNAME"),
    "_skins": ["Create a new skin"],
    "_skins_path": "",
    "_layouts": {},
    "_layout_path": "",
    "_year": time.strftime("%Y", time.localtime()),
}


def read_config(file_path):
    parser = configparser.ConfigParser(default_section="Rainmeter")
    try:  # trys to open file with default utf-8 encoding
        parser.read(file_path)
    except configparser.MissingSectionHeaderError:
        # This exception on this file likely means encoding is utf-16
        parser.read(file_path, encoding="utf-16")
    finally:
        return parser


rm_reg_key = None
try:
    rm_reg_key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        "SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Rainmeter",
    )
except FileNotFoundError:
    print("Rainmeter is not installed!")


def main():
    """Gathers default data before prompting user for input."""
    if rm_reg_key is not None:
        defaults["req_rainmeter_version"] = winreg.QueryValueEx(
            rm_reg_key, "DisplayVersion"
        )
        defaults["req_rainmeter_version"] = defaults["req_rainmeter_version"][
            0
        ].replace(" r", ".")
        defaults["_layout_path"] = os.getenv("APPDATA") + os.sep + "Rainmeter\\Layouts"

        # get path to Rainmeter skins
        parsed = read_config(os.getenv("APPDATA") + "\\Rainmeter\\Rainmeter.ini")
        if "Rainmeter" in parsed and "SkinPath" in parsed["Rainmeter"]:
            if parsed["Rainmeter"]["SkinPath"].endswith(os.sep):
                # remove trailing path seperator
                defaults["_skins_path"] = parsed["Rainmeter"]["SkinPath"][:-1]
            else:
                defaults["_skins_path"] = parsed["Rainmeter"]["SkinPath"]

        # grab names of installed skins
        if len(defaults["_skins_path"]):
            for d in os.listdir(defaults["_skins_path"]):
                if not d.startswith("@"):
                    # ignore @Backup & @Vault folders
                    defaults["_skins"].append(d)

        # now collect layouts
        for d in os.listdir(defaults["_layout_path"]):
            # read layout files in subfolders
            parsed = read_config(
                defaults["_layout_path"] + os.sep + d + os.sep + "Rainmeter.ini"
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
            defaults["_layouts"][d] = needed_skins

    # NOTE debugging output functions
    # dump to JSON
    with open("defaults.json", "w") as file:
        json.dump(defaults, file, indent=4)

    # print to console
    # for k, v in defaults.items():
    #     print("{} = {}".format(k, v))


if __name__ == "__main__":
    main()
    # now merge discovered defaults and begin cookie-cutting
    cookiecutter(".", output_dir="..", extra_context=defaults)

