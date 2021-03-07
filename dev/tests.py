from functools import partial

from invoke import task

from . import common, is_local_python, start

##############################################################################
# Test commands
##############################################################################


@task
def run(context, path="", p=""):
    """Run pytest tests with ``extra`` args for ``p`` tests.

    `p` means `params` - extra args for tests

    pytest <extra>
    """
    common.print_green(f"Tests {path} running.")
    execute = (
        context.run if is_local_python else partial(start.run_web, context=context)
    )
    execute(command=" ".join(["pytest", path, p]))


@task
def coverage(context, path=""):
    """Generate and display test-coverage."""
    common.print_green("Calculate and display code coverage")
    run(context, path=path, p="--cov")


@task
def e2e(context, path=""):
    """Runs end-to-end tests."""
    common.print_green("Runs end-to-end tests.")
    run(context, path=path, p="-m e2e")
