import os
import pwd
import grp
import stat

def get_user(user = None, path = None):
    if user == None:
        if path == None:
            uid = os.getuid()
        else:
            uid = os.stat(path).st_uid
        user_ = pwd.getpwuid(uid)

    elif type(user) == int:
        user_ = pwd.getpwuid(user).pw
    
    elif type(user) == str:
        user_ = pwd.getpwnam(user).pw_uid
    
    return user_


def get_group(group = None, path = None):
    if group == None:
        if path == None:
            uid = os.getuid()
            user_ = pwd.getpwuid(uid)
            gid = user_.pw_gid
        else:
            gid = os.stat(path).st_gid
        group_ = grp.getgrgid(gid)
        
    elif type(group) == int:
        group_ = grp.getgrgid(group)

    elif type(group) == str:
        group_ = grp.getgrnam(group)

    return group_


def convert_permissions(mode):
    permissions = ''
    for digit in mode:
        if digit == '7':
            permissions += 'rwx'
        elif digit == '6':
            permissions += 'rw-'
        elif digit == '5':
            permissions += 'r-x'
        elif digit == '4':
            permissions += 'r--'
        elif digit == '3':
            permissions += '-wx'
        elif digit == '2':
            permissions += '-w-'
        elif digit == '1':
            permissions += '--x'
        elif digit == '0':
            permissions += '---'
        else:
            raise Exception(f"Unexpected mode: '{mode}'")

    return permissions


# File types
FT_REGULAR = 'f'
FT_DIRECTORY = 'd'
FT_CHARACTER = 'c'
FT_BLOCK_DEVICE = 'b'
FT_NAMED_PIPE = 'p'
FT_SYMBOLIC_LINK = 'l'
FT_SOCKET = 's'

def find_file_type(path):
    file_stat = os.stat(path)
    mode = file_stat.st_mode
    if stat.S_ISREG(mode):
        return FT_REGULAR
    elif stat.S_ISDIR(mode):
        return FT_DIRECTORY
    elif stat.S_ISCHR(mode):
        return FT_CHARACTER
    elif stat.S_ISBLK(mode):
        return FT_BLOCK_DEVICE
    elif stat.S_ISFIFO(mode):
        return FT_NAMED_PIPE
    elif stat.S_ISLNK(mode):
        return FT_SYMBOLIC_LINK
    elif stat.S_ISSOCK(mode):
        return FT_SOCKET
    else:
        raise Exception(f"Unknown file type: {path}")