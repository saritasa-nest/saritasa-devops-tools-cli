import json
import os

from invoke import task

from marina.aws.iam import list_roles
from marina.clients.saritasa import SaritasaInfraV2

from . import common, docker, start, system

##############################################################################
# Django commands and stuff
##############################################################################

__all__ = ("find_roles",)

##############################################################################
# Roles
##############################################################################


@task
def find_roles(context, pattern=None):
    """Find roles by pattern name."""
    roles = list_roles(acc=SaritasaInfraV2(), pattern=pattern)
    print(json.dumps(roles))
