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
    "import_skin": ["Create a new skin"],
    "_skins_path": "",
    "_year": time.strftime('%Y', time.localtime())
}

parser = configparser.ConfigParser()

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
        try:  # trys to open file with default utf-8 encoding
            parser.read(os.getenv("APPDATA") + "\\Rainmeter\\Rainmeter.ini")
        except configparser.MissingSectionHeaderError:
            # This exception on this file likely means encoding is utf-16
            parser.read(
                os.getenv("APPDATA") + "\\Rainmeter\\Rainmeter.ini", encoding="utf-16"
            )

        if "Rainmeter" in parser and "SkinPath" in parser["Rainmeter"]:
            if parser["Rainmeter"]["SkinPath"].endswith(os.sep):
                # remove trailing path seperator
                defaults["_skins_path"] = parser["Rainmeter"]["SkinPath"][:-1]
            else:
                defaults["_skins_path"] = parser["Rainmeter"]["SkinPath"]

        # defaults["_skins_path"] = defaults["_skins_path"]
        if len(defaults["_skins_path"]):
            for d in os.listdir(defaults["_skins_path"]):
                if not d.startswith("@"):
                    defaults["import_skin"].append(d)

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

