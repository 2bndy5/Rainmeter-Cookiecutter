# Rainmeter-Cookiecutter

A [cookiecutter] template repository for developing Rainmeter Skin(s)
via github.

## Features

* Integrated Github workflow (includes a badge) for building and
  uploading a Rainmeter Skin Package (a
  `<repo-name>_<version_tag>.rmskin` file) to your published
  releases for easy installation.
* An extra workflow (includes a badge) to scan the repository for
  malicious software using ClamAV. This is useful if your repository
  contains executable binaries like 3rd-party Rainmeter plugins or
  exe files. That said, it is still *strongly recommended* that you
  monitor what executable binary files get added to your repository.
* License options include GNU GPLv3, CC BY-SA-4.0, or MIT.
* Ability to import an installed Rainmeter Skin or a Layout of Skins.
  
  If importing a Skin:
  
  * Only 1 skin can be specified if importing a skin during the
    [cookiecutter] process, but more can be added after
    [cookiecutter] has finished generating your repository.
  * User input must specify what skin (from a numbered list of
    choices) to load when the released rmskin package is installed.

  If importing a Layout:
  
  * All active skins in the Layout are imported as well as the Layout file.
  * The Layout is automatically set to load when the released rmskin package is installed

* If not importing a skin or layout (default option), then [cookiecutter]
  will create a new skin using the "project name" (also specified by
  the user) as the Skin's name (with root config `<project_name>.ini`
  file & `Variables.inc` file in the skin's `@Resources` folder).
  The newly created skin's .ini file is automatically set to load when
  the released rmskin package is installed.
* A `README.rst` file to greet github-browsing users, and includes
  instructions on how to install your Rainmeter Project
* A `RMSKIN.ini` file for creating a valid `rmskin` file. This
  file would rarely get altered as the "RMSKIN Packager" workflow
  attempts to fill in the missing information from github
  environment variables.
* Choose minimum required Windows version which is automatically limited to
  only the versions supported by the specified minimum required version of
  Rainmeter.

> [!TIP]
> Read the comments in the `RMSKIN.ini` file to better understand what it is used for.

## How To Use

This [cookiecutter] template repository is a little different from
your usual [cookiecutter] template repositories. To gather information
about your local system's Rainmeter installation, you must start the
[cookiecutter] process by running the `cut_cookie.py` script located at
the root folder of this repository.

> [!NOTE]
> The [`cookiecutter`][cookiecutter] command is the conventional method for
> typical cookiecutter templates. But, it does not get data about your
> local system's Rainmeter installation. Furthermore, this template's
> `cut_cookie.py` script overrides the [`cookiecutter`][cookiecutter]
> command's user input process so that it can provide a slightly more
> complex sequence of options to the user.

It is recommend using a Python virtual environment with
[`cookiecutter`][cookiecutter] installed.
This is easily done in 1 command using [`uv`][uv] or [`pipx`][pipx].

### Using [`pipx`][pipx]

```shell
pipx run --path cut_cookie.py
```

### Using [`uv`][uv]

```shell
uv run --script cut_cookie.py
```

[uv]: https://docs.astral.sh/uv/
[pipx]: https://pipx.pypa.io/stable/
[cookiecutter]: https://cookiecutter.readthedocs.io/
