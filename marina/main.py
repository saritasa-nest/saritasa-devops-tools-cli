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
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug

    if account_id or account_alias:
        account_klass = get_account_class(id=account_id, alias=account_alias)
        if not account_klass:
            click.echo("Unable to find the account")
            exit(1)
        ctx.obj["ACCOUNT_ID"] = account_id
        ctx.obj["ACCOUNT_ALIAS"] = account_alias
        ctx.obj["ACCOUNT"] = account_klass()


@cli.command()
@click.pass_context
@click.option("--pattern", help="IAM role name pattern to search for")
def iam_find_roles(ctx, pattern):
    """IAM - Find roles by pattern in name."""
    roles = list_roles(acc=ctx.obj["ACCOUNT"], pattern=pattern)
    print(json.dumps(roles))


@cli.command()
@click.pass_context
@click.option("--category", help="Category (worktype or framework) to get default secrets structure for")
def secrets_defaults(ctx, category):
    """Secrets - Get default structure values."""

    common_backend = [
        "aws_s3_direct_region",
        "aws_s3_bucket_name",
        "app_debug",
        "email_host",
        "email_host_password",
        "email_host_port",
        "email_host_use_tls",
        "email_host_user",
        "rds_db_host",
        "rds_db_name",
        "rds_db_password",
        "rds_db_port",
        "rds_db_user",
        "redis_host",
        "redis_port",
        "updated",
    ]

    _defaults = {
        "django": [
            "django_secret_key",
            "django_secret_salt",
        ]
        + common_backend,
        "laravel": [
            "laravel_secret_key",
            "laravel_secret_salt",
        ]
        + common_backend,
        "backend": common_backend,
        "frontend": ["api_path", "updated"],
    }

    defaults = {}

    for d in _defaults:
        defaults[d] = { k:"set in secret manager" for k in _defaults[d] }

    if category:
        ret = defaults.get(category, {})
        print(json.dumps(ret))
    else:
        print(json.dumps(defaults))
        

    

if __name__ == "__main__":
    cli(obj={})
