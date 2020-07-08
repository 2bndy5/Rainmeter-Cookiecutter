Introduction
============

A cookiecutter template reository for developing Rainmeter Skin(s)
via github.

Features
========

* Integrated Github workflow (includes a badge) for building and
  uploading a Rainmeter Skin Package (a
  ``<repo-name>_<version_tag>.rmskin`` file) to your published
  releases for easy installation.
* An extra workflow (includes a badge) to scan the repository for
  malicious software using ClamAV. This is useful if your reository
  contains executable binaries like 3rd-party Rainmeter plugins or
  exe files.
* License options include GNU GPLv3, CC BY-SA-4.0, or MIT.
* Ability to import an installed Rainmeter Skin. Only 1 skin can be
  specified during cookiecutter process, but more can be added after
  cookiecutter has finished generating your repository.
* If not importing a skin, then cookiecutter will create a new skin
  using the repository name as the Skin's name (with root config
  ``<repo-name>.ini`` file & ``Variables.inc`` file in the skin's
  ``@Resources`` folder)
* A ``README.rst`` file to greet github-browsing users, and includes
  instructions on how to install your Rainmeter Project
* A ``RMSKIN.ini`` file for creating a valid ``rmskin`` file. This
  file would rarely get altered as the "RMSKIN Packager" workflow
  attempts to fill in the missing information from github
  environment variables.

  .. tip:: Read the comments in the ``RMSKIN.ini`` file to better
    understand what it is used for.

How To Use
==========

This cookiecutter template repository is a little different from
your usual cookiecutter template repositories. To gather information
about your local system's Rainmeter installation, you must start the
cookiecutter process by typing the following at root folder of this
repository:

.. code-block:: shell

    pip install -r requirements.txt
    python cutcookie.py

If don't start the process with the above command, then you will not
have certain options available. These options include picking an
installed skin to import, finding the currently installed version
of Rainmeter, and identifying the current year for licensing. If
for some reason the above command does not work, please submit an
issue and try the following at root folder of this repository:

.. code-block:: shell

    pip install -r requirements.txt
    cookiecutter

.. note:: The second command is the conventional method, but does
    not get data about your local system's Rainmeter installation.
    Also make sure that Python's script folder (defaults to
    ``%APPDATA%\Python\Python3x\Scripts`` where 3x is the version of
    python you have installed) is in your Windows environment
    variable, ``PATH``. Otherwise, try ``python -m cookiecutter``.