from invoke import task

from . import common


class InvokeNetworkException(Exception):
    """Docker networking exception

    Used to bypass fatal error of invoke cli execution
    in the case desired docker network is already created
    """

    pass


##############################################################################
# Containers start stop commands
##############################################################################

__all__ = (
    "docker_compose_run",
    "docker_compose_start",
    "docker_compose_up",
    "run_containers",
    "stop_containers",
    "docker_run",
)


def docker_run(context, command):
    """Run ``command`` using docker

    docker run <command>
    """
    return context.run(" ".join(["docker", "run", "-it --rm", command]))


def docker_compose_up(context, command):
    """Up ``command`` using docker-compose

    docker-compose up <command>

    Used function so lately it can be extended to use different docker-compose
    files
    """
    common.print_green("Up {} containers ".format(command))
    return context.run(" ".join(["docker-compose", "up", command]))


def docker_compose_start(context, command):
    """Start ``command`` using docker-compose

    docker-compose start <command>

    Used function so lately it can be extended to use different docker-compose
    files
    """
    common.print_green("Start {} containers ".format(command))
    return context.run(" ".join(["docker-compose", "start", command]))


def docker_compose_run(context, command):
    """Run ``command`` using docker-compose

    docker-compose run <command>

    Used function so lately it can be extended to use different docker-compose
    files
    """
    return context.run(" ".join(["docker-compose", "run", "--rm", command]))


def docker_compose_exec(context, service, command):
    """Run ``exec`` using docker-compose

    docker-compose run <command>

    Used function so lately it can be extended to use different docker-compose
    files
    """
    return context.run(" ".join(["docker-compose", "exec", service, command]))


def run_containers(context, *containers, **kwargs):
    """Run containers"""
    common.print_green("Start {} containers ".format(containers))
    context.run(
        " ".join(
            ["docker-compose", "up", "-d" if kwargs.get("d") else ""] + list(containers)
        )
    )


def stop_containers(context, *containers):
    """Stop containers"""
    common.print_green("Stopping {} containers ".format(containers))
    context.run(" ".join(["docker-compose", "stop"] + list(containers)))


##############################################################################
# Containers networking
##############################################################################


def create_network(context, network=None):
    """Create docker network"""
    if not network:
        return None

    common.print_green("Create {} network".format(network))

    try:
        context.run(
            "docker network create {}".format(network),
            warn=True,
        )
    except InvokeNetworkException:
        pass
