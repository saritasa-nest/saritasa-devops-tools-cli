import json

import click

from marina.aws.iam import list_roles
from marina.clients import get_account_class


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option("--account-id", default=None, help="AWS Account ID to search in")
@click.option("--account-alias", default=None, help="AWS Account ID Alias to search in")
@click.pass_context
def cli(ctx, debug, account_id, account_alias):
    """CLI entrypoint."""
    account_klass = get_account_class(id=account_id, alias=account_alias)

    if not account_klass:
        click.echo("Unable to find the account")
        exit(1)

    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug
    ctx.obj["ACCOUNT_ID"] = account_id
    ctx.obj["ACCOUNT_ALIAS"] = account_alias
    ctx.obj["ACCOUNT"] = account_klass()


@cli.command()
@click.pass_context
@click.option("--pattern", help="IAM role name pattern to search for")
def iam_find_roles(ctx, pattern):
    """IAM. Find roles by pattern in name."""
    roles = list_roles(acc=ctx.obj["ACCOUNT"], pattern=pattern)
    print(json.dumps(roles))


if __name__ == "__main__":
    cli(obj={})
