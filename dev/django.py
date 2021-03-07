import os

from invoke import task

from . import common, docker, start, system

##############################################################################
# Django commands and stuff
##############################################################################

__all__ = (
    "manage",
    "makemigrations",
    "migrate",
    "resetdb",
    "run",
    "shell",
    "dbshell",
)


@task
def manage(context, command):
    """Run ``manage.py`` command.

    docker-compose run --rm web python3 manage.py <command>

    """
    return start.run_python(context, " ".join(["manage.py", command]))


@task
def makemigrations(context):
    """Run makemigrations command and chown created migrations"""
    common.print_green("Django: Make migrations")
    manage(context, "makemigrations")
    system.chown(context)


@task
def migrate(context):
    """Run ``migrate`` command"""
    common.print_green("Django: Apply migrations")
    manage(context, "migrate")


@task
def resetdb(context):
    """Reset database to initial state (including test DB)"""
    common.print_green("Reset database to its initial state")
    manage(context, "drop_test_database --noinput")
    manage(context, "reset_db -c --noinput")
    makemigrations(context)
    migrate(context)
    createsuperuser(context)


@task
def createsuperuser(context):
    """Create superuser"""
    common.print_green("Create superuser")
    manage(context, "createsuperuser")


@task
def run(context):
    """Run development web-server"""

    # start dependencies (so even in local mode this command
    # is working successfully
    # if you need more default services to be started define them
    # below, like celery, etc.
    docker.docker_compose_start(context, "postgres redis")
    try:
        env = os.environ["ENVIRONMENT"]  # noqa
    except KeyError:
        common.print_red(
            "Please set the environment variable " "ENVIRONMENT, like=local"
        )
        exit(1)
    common.print_green("Running web app")
    start.run_python(
        context, "manage.py runserver_plus 0.0.0.0:8000  --reloader-type stat"
    )


@task
def shell(context, params=None):
    """Shortcut for manage.py shell_plus command

    Additional params available here:
        http://django-extensions.readthedocs.io/en/latest/shell_plus.html
    """
    common.print_green("Entering Django Shell")
    manage(context, "shell_plus --ipython {}".format(params or ""))


@task
def dbshell(context):
    """Open postgresql shell with credentials from either local or dev env"""
    common.print_green("Entering DB shell")
    manage(context, "dbshell")
