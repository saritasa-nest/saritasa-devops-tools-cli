from marina.aws.accounts import AWSAccount


class SaritasaInfraV2(AWSAccount):
    """Saritasa Infra V2 Account."""

    account_id = "965067289393"
    account_alias = "saritasa-infra-v2"
    assume_role_arn = (
        "arn:aws:iam::965067289393:role/OrganizationAccountAccessRole"  # noqa
    )
