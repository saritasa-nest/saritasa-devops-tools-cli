from marina.aws.accounts import registered_accounts

from .saritasa import *


def get_account_class(id: str = None, alias: str = None):
    """Get AWSAccount class either by AWS Account ID or given alias."""
    return registered_accounts["by_id"].get(
        id, registered_accounts["by_alias"].get(alias)
    )
