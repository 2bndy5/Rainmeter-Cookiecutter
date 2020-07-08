.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/workflows/Anti-virus%20Check/badge.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/actions?query=workflow%3A%22Anti-virus+Check%22

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/workflows/RMSKIN%20Package/badge.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/actions?query=workflow%3A%22RMSKIN+Packager%22

.. image:: https://img.shields.io/github/v/release/rainmeter/rainmeter?label=Rainmeter&logo=github&style=plastic
    :alt: Rainmeter Required (latest stable)
    :target: https://github.com/rainmeter/rainmeter/releases/latest

.. image:: https://img.shields.io/github/license/blah-name/blah-repo?style=plastic
    :alt: license

{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}#{% endfor %}

This is the home for developing {{ cookiecutter.project_name }}. {{ cookiecutter.short_description }}

Rainmeter required
##################

The minimum required version of Rainmeter is {{ cookiecutter.req_rainmeter_version }}, but the `latest stable release <https://www.rainmeter.net>`_ is recommended.

Package Installer
#################

`This repository's releases <https://github.com/
{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/
releases>`_ include a Rainmeter package file called
``{{ cookiecutter.project_name }}_<version>.rmskin``. Open this file
with Rainmeter, follow the prompts, and the packaged files will be
copied/installed appropriately to your Rainmeter skins folder.


Manual Install
##############

Download this repository's zip file and extract the folder
``{{ cookiecutter.project_name }}`` (located in ``Skins``
folder) into the Rainmeter skins folder (defualts to
``C:\Users\%USERNAME%\Documents\Rainmeter\skins`` -
unless onedrive manages your user documents folder). If
installing a Rainmeter layout, the aforementioned
`Package Installer`_ is preferred and highly recommended.