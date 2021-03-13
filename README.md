# README

Simple CLI tools for devops team

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
export PYTHONPATH=`pwd`
python3 marina/main.py --help
```

## Build the package

```bash
python3 -m pip install --upgrade build
python3 -m build
```

## Test locally

```bash
git clone git@github.com:saritasa-nest/saritasa-devops-tools-cli.git
cd /some/folder
pip3 install /home/dmitry/Projects/_saritasa/saritasa-devops-tools-cli
marina --account-alias=saritasa-infra-v2  iam-find-roles --pattern SSO | jq
```

Keep in mind your SHELL should have proper AWS env vars set, as we do not pass AWS secrets to marina CLI:

```bash
AWS_ACCESS_KEY_ID=YOURKEY
AWS_SECRET_ACCESS_KEY=YOURSECRET
AWS_DEFAULT_REGION=us-west-2
AWS_DEFAULT_OUTPUT=table
```
