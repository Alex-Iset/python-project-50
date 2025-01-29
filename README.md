<a href="https://ru.hexlet.io/">
<p align="center">
    <img src="images/hexlet_logo.png" 
        width="200" 
        height="200">
</p>
</a>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Alex-Iset/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Alex-Iset/python-project-50/actions)
[![my-check](https://github.com/Alex-Iset/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/Alex-Iset/python-project-50/actions/workflows/my-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c8e085926eb96f710b45/maintainability)](https://codeclimate.com/github/Alex-Iset/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c8e085926eb96f710b45/test_coverage)](https://codeclimate.com/github/Alex-Iset/python-project-50/test_coverage)


### Tech Stack:
![Static Badge](https://img.shields.io/badge/python-3.12-F?style=flat&logo=python&color=yellow)
![Static Badge](https://img.shields.io/badge/pipx-1.4.3-F?style=flat&logo=pipx&color=00D8AD)
![Static Badge](https://img.shields.io/badge/uv-0.5.8-F?style=flat&logo=uv&color=9001CD)
![Static Badge](https://img.shields.io/badge/pyyaml-6.0.2-F?style=flat&color=yellow)


## Table of contents:
### [1. «Difference Calculator»](#difference-calculator)
### [2. Install (Linux)](#install-linux)
### [3. How to use?](#how-to-use)


## «Difference Calculator»:
«Difference Calculator» -  is a program that determines the difference between two data structures. 
This is a popular task, for which there are many online services, such as jsondiff. 
A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.
Utility features:
* Support for different input formats: yaml, json
* Generating a report in plain text, stylish, and json format


## Install (Linux):
1. Install pipx
```
sudo apt install pipx
```
2. Install uv
```
pipx install uv
```
3. Cloning a repository
```
git clone https://github.com/Alex-Iset/python-project-50.git
```
4. Going to the "python-project-50" directory
```
cd python-project-50
```
5. Initializing the python-package inside the root directory of the project
```
uv init
```
6. Creating a virtual environment
```
uv env
```
7. Getting the version of all packages installed in the project
```
uv sync
```

## How to use?
To get help on how to use the utility, 
you can use uv scripts:
```
uv run gendiff -h
```
or Makefile commands:
```
make run-help
```
There is also an option to launch utility by creating a distribution kit and installing it:
```
make build
make package-install
```
Utility can now be run with shorter commands:
```
gendiff -h
```
To see a demonstration of how the utility works with your own hands, 
you can use the Makefile commands:
```
make run-stylish
make run-plain
make run-json
```