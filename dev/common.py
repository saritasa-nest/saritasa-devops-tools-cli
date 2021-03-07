from functools import partial

from termcolor import colored

green = partial(colored, color="green")
red = partial(colored, color="red")


def message(text):
    """Format message
    Args:
        text (str): textual message to format
    """
    length = len(text) if len(text) > 76 else 76

    msg = "\n"
    msg += "o" * (length + 4) + "\n"
    msg += "o {:76s} o\n".format(text)
    msg += "o" * (length + 4) + "\n"
    return msg


def print_green(msg, box=True):
    if box:
        return print(green(message(msg)))
    return print(green(msg))


def print_red(msg, box=True):
    if box:
        return print(red(message(msg)))
    return print(red(msg))
