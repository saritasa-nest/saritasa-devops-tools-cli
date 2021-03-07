# README

## Project-related links

* [Project repository](https://github.com/saritasa-nest/saritasa-devops-tools-cli)
* [Upsource]()

## Requirements

### Python version

The project uses Python v3.8.6.

### Tools

The following tools required:
  * [docker](https://docs.docker.com/install/).
    Ensure you can run `docker` without `sudo`;
  * [pip](https://pypi.org/project/pip/)
  * [invoke](https://pypi.org/project/invoke/).
  * [pyenv](https://github.com/pyenv/pyenv).
  * [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).    

## Project development

To build the project, run:

```bash
pyenv install 3.8.6
pyenv virtualenv 3.8.6 saritasa-devops-tools
git clone git@github.com:saritasa-nest/saritasa-devops-tools-cli.git
cd saritasa-devops-tools-cli
pyenv activate saritasa-devops-tools
pyenv local saritasa-devops-tools
pip install -U pip pip-tools setuptools
pip install -U click invoke pyyaml requests prompter emoji yaspin termcolor
pip install -r requirements/development.txt
inv dev.requirements-install
```

## Build the package

```bash
python3 -m pip install --upgrade build
python3 -m build
```