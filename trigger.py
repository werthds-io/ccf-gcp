import os
from functools import wraps


def on_new_commit(func):

    @wraps(funct)
    def wrapper(*args, **kwargs):
        #checks if commit hash changed
        if cache.get_commit() != os.getenv("GITHUB_SHA"):
            func(*args, **kwargs)

    return wrapper


@on_new_commit
def deploy_app(*args):
    print("Deploying application")
