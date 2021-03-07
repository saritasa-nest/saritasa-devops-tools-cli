import os
import re
from functools import partial
from typing import List

from invoke import task

from . import common, is_local_python, start

##############################################################################
# Build project locally
##############################################################################

__all__ = (
    "requirements_compile",
    "requirements_install",
    "isort",
    "lint_pycodestyle",
    "lint_pylama",
    "lint_flake8",
    "lint_all",
)


##############################################################################
# Manage dependencies
##############################################################################


@task
def requirements_compile(context, u=True):
    """Compile requirements with pip-tools"""
    # pip-tools upgrades packages by default
    upgrade = "-U" if u else ""
    environments = [
        "development",
        "staging",
        "production",
    ]

    for environment in environments:
        common.print_green(f"Compile requirements/{environment}.in")
        context.run(
            f"pip-compile requirements/{environment}.in {upgrade} "
            f"--output-file requirements/{environment}.txt"
        )


@task
def requirements_install(context, u=True):
    """Install requirements with pip-tools"""
    # pip-tools upgrades packages by default
    upgrade = "-U" if u else ""

    common.print_green(f"Install requirements/development.txt")
    context.run("pip install --upgrade pip")
    context.run("pip install -r requirements/development.txt")


##############################################################################
# Linters
##############################################################################

DEFAULT_FOLDERS = "marina"


def run_isort(context, path=None):
    """Sorts python imports by the specified path.

    Args:
        path(str): Path to selected file

    Usage:
        # is simple mode without report
        inv linters.isort
        # usage on selected file
        inv linters.isort --path='apps/users/models.py'

    """
    context.run("isort {path}".format(path=path))


@task
def isort(context, path=None, print_msg=True):
    """Command to fix imports formatting."""
    if print_msg:
        print("Running imports fix\n")
    return run_isort(context, path) if path else run_isort(context, ".")


@task
def lint_pycodestyle(context, path=None):
    """Check code style by `pycodestyle` tool raise the `Aborting` exception
    with error code for avoid the error message used the `warn_only` for pep8
    used `setup.cfg` configuration file

    Args:
        path(str): Path to selected file

    Usage:
        # is simple mode without report
        inv linters.pep8
        # usage on selected file
        inv linters.pep8 --path='apps/users/models.py'

    """
    common.print_green("Linters: Pycodestyle (ex PEP8) running")
    execute = (
        context.run if is_local_python else partial(start.run_web, context=context)
    )
    return execute(command=f"pycodestyle {path if path else DEFAULT_FOLDERS}")


@task
def lint_pylama(context, path=None):
    """Check codestyle by `pylama` inv file raise the `Aborting` exception with
    error code for avoid the error message used the `warn_only` for pylama used
    `setup.cfg` configuration file.

    Args:
        path(str): Path to selected file

    Usage:
        # is simple mode without report
        inv linters.pylama
        # usage on selected file
        inv linters.pylama --path='apps/users/models.py'

    """
    common.print_green("Linters: Pylama running")
    execute = (
        context.run if is_local_python else partial(start.run_web, context=context)
    )
    return execute(command=f"pylama {path if path else DEFAULT_FOLDERS}")


@task
def lint_flake8(context, path=None):
    """Check code style by `flake8` inv file raise the `Aborting` exception
    with error code for avoid the error message used the `warn_only` for flake8
    used `setup.cfg` configuration file.

    Args:
        path(str): Path to selected file

    Usage:
        # is simple mode without report
        inv linters.flake8
        # usage on selected file
        inv linters.flake8 --path='apps/users/models.py'

    """
    common.print_green("Linters: Flake8 running")
    execute = (
        context.run if is_local_python else partial(start.run_web, context=context)
    )
    return execute(command=f"flake8 {path if path else DEFAULT_FOLDERS}")


@task
def lint_all(context, path=None):
    """Run all linters (isort, pycodestyle, pylama, flake8).

    Args:
        path(str): Path to selected file

    Usage:
        # is simple mode without report
        inv linters.all
        # usage on selected file
        inv linters.all --path='apps/users/models.py'

    """
    linters = (isort, lint_pycodestyle, lint_pylama, lint_flake8)
    for linter in linters:
        linter(context, path=path) if path else linter(context)
