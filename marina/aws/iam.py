from .accounts import AWSAccount


def list_roles(acc: AWSAccount, pattern: str):
    """Get IAM Roles matching the pattern."""
    roles = []
    roles_all = []

    # Use the temporary credentials that AssumeRole returns to make a
    # connection to Amazon S3
    iam_client = acc.get_client("iam")
    response = iam_client.list_roles(PathPrefix="/", MaxItems=1000)
    roles_all.extend(response["Roles"])

    # it's possible AWS truncates the results, so we should make sure
    # to send additional requests to get ALL records through API
    while "Marker" in response.keys():
        response = iam_client.list_roles(Marker=response["Marker"])
        roles_all.extend(response["Roles"])

    for role in roles_all:
        role_name = role["RoleName"]
        if pattern:
            if pattern in role_name:
                del role["CreateDate"]
                roles.append(role)
        else:
            del role["CreateDate"]
            roles.append(role)

    if len(roles) == 1:
        return roles.pop()
    return roles
