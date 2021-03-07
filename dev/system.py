from invoke import task

from . import common

##############################################################################
# System shortcuts
##############################################################################


def chown(context):
    """Shortcut for owning apps dir by current user after some files were
    generated using docker-compose (migrations, new app, etc)
    """
    context.run("sudo chown ${USER}:${USER} -R apps")


def gitmessage(context):
    """Set default .gitmessage"""
    common.print_green("Deploy git commit message template")
    context.run('echo "[commit]" >> .git/config')
    context.run('echo "  template = .gitmessage" >> .git/config')


@task
def hooks(context):
    """Install git hooks

    Used during ``build``
    """
    common.print_green("Changing git hook default directory to .git-hooks")
    context.run("git config core.hooksPath .git-hooks")
