import grp
from sysadmin import utils


def id(user=None):
    try:
        user_ = utils.get_user(user)
    except:
        raise Exception(f"id: '{user}': no such user")

    gid = user_.pw_gid

    output = {
        "user": {
            "uid":user_.pw_uid,
            "username": user_.pw_name
        },
        "primary_group": {
            "gid":user_.pw_gid,
            "groupname":grp.getgrgid(gid).gr_name
        },
    }
    output["allgroups"] = [output["primary_group"]]

    for group in grp.getgrall():
        if user_.pw_name in group.gr_mem:
            output["all_groups"].append({
                "gid": group.gr_gid,
                "group_name": group.gr_name
            })

    return output    


def adduser():
    pass

def usermod():
    pass

def deluser():
    pass

def addgroup():
    pass

def delgroup():
    pass

def passwd(secret):
    pass

def chage():
    pass
