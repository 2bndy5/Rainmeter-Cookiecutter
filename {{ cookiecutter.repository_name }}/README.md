# {{ cookiecutter.project_name }}

<!-- markdownlint-disable MD034 MD052 -->
[![anti-virus-check][anti-virus-ci-badge]][anti-virus-ci-link]
[![RMSKIN packager][rmskin-ci-badge]][rmskin-ci-link]
[![Rainmeter Required (latest stable)][rainmeter-ver-badge]][rainmeter-link]
[![license][license-badge]][license-link]

This is the home for developing {{ cookiecutter.project_name }}. {{ cookiecutter.short_description }}

## Rainmeter required

The minimum required version of Rainmeter is {{ cookiecutter.req_rainmeter_version }}, but the `latest stable release <https://www.rainmeter.net>`_ is recommended.

## Package Installer

[This repository's releases][releases] include a Rainmeter package file called
`{{ cookiecutter.project_name }}_<version>.rmskin`.
Open this file with Rainmeter, follow the prompts, and the packaged files will be
copied/installed appropriately to your Rainmeter skins folder.

## Manual Install

Download this repository's zip file and extract the folder
`{{ cookiecutter.project_name }}` (located in `Skins`
folder) into the Rainmeter skins folder (defaults to
`C:\Users\%USERNAME%\Documents\Rainmeter\skins` -
unless OneDrive manages your user documents folder). If
installing a Rainmeter layout, the aforementioned
[Package Installer](#package-installer) is preferred and highly recommended.

[anti-virus-ci-badge]: "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/workflows/Anti-virus%20Check/badge.svg"
[anti-virus-ci-link]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/actions?query=workflow%3A%22Anti-virus+Check%22
[rmskin-ci-badge]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/workflows/RMSKIN%20Packager/badge.svg
[rmskin-ci-link]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/actions?query=workflow%3A%22RMSKIN+Packager%22
[rainmeter-ver-badge]: https://img.shields.io/github/v/release/rainmeter/rainmeter?label=Rainmeter&style=plastic&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2LjM1IDYuMzUiIGhlaWdodD0iMjQiIHdpZHRoPSIyNCI+PHRleHQgeT0iNi4zNSIgc3R5bGU9ImxpbmUtaGVpZ2h0OjEuMjU7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonU2Vnb2UgTURMMiBBc3NldHMnIiBmb250LXNpemU9IjYuMzUiIGZvbnQtZmFtaWx5PSJTZWdvZSBNREwyIEFzc2V0cyIgZmlsbD0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIuMjY1Ij48dHNwYW4geT0iNi4zNSIgeD0iMCI+7q2CPC90c3Bhbj48L3RleHQ+PC9zdmc+
[rainmeter-link]: https://github.com/rainmeter/rainmeter/releases/latest
[license-badge]: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}?color=blue&style=plastic&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PGRlZnM+PHBhdGggaWQ9ImIiIGQ9Ik0tMTUuMzc0IDgzLjUwOWg0Ni42NDZ2NDAuMTgyaC00Ni42NDZ6Ii8+PHBhdGggaWQ9ImEiIGQ9Ik0tNy44NjIgOTcuMzExaDI5Ljg3NVYxMTguOEgtNy44NjJ6Ii8+PC9kZWZzPjx0ZXh0IHk9IjI0IiBzdHlsZT0ibGluZS1oZWlnaHQ6MS4yNTstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidTZWdvZSBNREwyIEFzc2V0cyciIGZvbnQtc2l6ZT0iMjQiIGZvbnQtZmFtaWx5PSJTZWdvZSBNREwyIEFzc2V0cyIgZmlsbD0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIuMjgxIj48dHNwYW4geT0iMjQiIHg9IjAiPu6GkjwvdHNwYW4+PC90ZXh0Pjwvc3ZnPg==
[license-link]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/blob/master/LICENSE
[releases]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}/releases>
