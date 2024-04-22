import os
from sysadmin import utils

# TODO - recursive chown
def chown(path: str, recursive: bool = False, user: int | str | None = None, group: int | str | None = None) -> None:
    """
    Change the owner and group of a file or directory.

    """
    if not os.path.exists(path):
        raise Exception(f"chown: cannot access '{path}': No such file or directory")
    
    if (user == None) and (group == None):
        raise Exception(f"chown: user or group is missing")

    user_ = utils.get_user(user, path)
    gid, _ = utils.get_group(group, path)

    os.chown(path, user_.pw_uid, gid)


def chmod(path: str, perm: int | str, recursive: bool = False):
    pass


def getfacl(path: str):
    pass


def setfacl(path: str, recursive: bool = False, modify: bool = False):
    pass

chown("/root/apps/mini-python-projects/linux_lib/testfile", user=0, group=1000)