
from apps.users.models import User, LoginHistory
from apps.posts.models import RequestHistory


def replace_none_with_empty_str(some_dict):
    return {k: ('' if v is None else v) for k, v in some_dict.items()}


def update_login_history(username, successful):
    data = {
        "user": User.objects.get(username=username),
        "successful": successful}

    args = replace_none_with_empty_str(data)

    return LoginHistory.objects.create(**args)


def update_request_history(username, endpoint, successful):
    data = {
        "user": User.objects.get(username=username),
        "endpoint": endpoint,
        "successful": successful}

    args = replace_none_with_empty_str(data)

    return RequestHistory.objects.create(**args)
