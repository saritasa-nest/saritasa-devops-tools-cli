import boto3

# registry of available AWS accounts
registered_accounts = {"by_id": {}, "by_alias": {}}


def register_account_id(id: str, klass):
    """Register AWS Account class by AWS Account ID."""
    registered_accounts["by_id"][id] = klass


def register_account_alias(alias: str, klass):
    """Register AWS Account class by AWS Alias declared in the class."""
    registered_accounts["by_alias"][alias] = klass


class AWSAccount(object):
    """Abstract AWS Account."""

    def __init_subclass__(cls, **kwargs):
        """Init subclass into registry."""
        if hasattr(cls, "account_id"):
            register_account_id(cls.account_id, cls)
        if hasattr(cls, "account_alias"):
            register_account_alias(cls.account_alias, cls)

    def get_credentials(self):
        """Get temporary credentials.

        The calls to AWS STS AssumeRole must be signed with the access key ID
        and secret access key of an existing IAM user or by using existing
        temporary credentials such as those from another role. (You cannot call
        AssumeRole with the access key for the root account.) The credentials
        can be in environment variables or in a configuration file and will be
        discovered automatically by the boto3.client() function. For more
        information, see the Python SDK documentation:
        http://boto3.readthedocs.io/en/latest/reference/services/sts.html#client
        """
        # create an STS client object that represents a live connection to the
        # STS service
        sts_client = boto3.client("sts")

        # Call the assume_role method of the STSConnection object and pass the
        # role ARN and a role session name.
        assumed_role_object = sts_client.assume_role(
            RoleArn=self.assume_role_arn,
            RoleSessionName="saritasa-devops-python",
        )

        # From the response that contains the assumed role, get the temporary
        # credentials that can be used to make subsequent API calls
        credentials = assumed_role_object["Credentials"]

        return dict(
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )

    def get_client(self, service_name: str):
        """Get boto3 client."""
        return boto3.client(service_name, **self.get_credentials())
