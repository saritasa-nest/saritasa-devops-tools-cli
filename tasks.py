import os
import sys
from importlib import util

from invoke import Collection

from dev import dev, django, docker, docs, iam, system, tests, tools

ns = Collection(
    iam,
    django,
    docker,
    docs,
    dev,
    system,
    tests,
    tools,
)

# Congigurations for run command
ns.configure({"run": {"pty": True, "echo": True}})

# let's load custom commands defined in
# ~/.invoke/my.py

sys.path.append(os.path.expanduser("~/.invoke"))

spec = util.find_spec("my")

# load custom invoke commands in the case such
# file exists
if spec:
    zzz = util.module_from_spec(spec)
    spec.loader.exec_module(zzz)
