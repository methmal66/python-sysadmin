from pwd import struct_passwd
from grp import struct_group
from typing import Literal
from typing_extensions import TypeAlias

def get_user(user: int | str | None = None, path: str | None = None) -> struct_passwd:
    '''
    Get a unix user from /etc/passwd database on different conditions

    Parameters:

        - user (optional): Uid(int) or username(str) of the user
        - path (optional): Relative file path(str) to find the owner

    Returns:

        - (struct_user) a user

    Usage::

        get_user()  # Get the user who is running the program
        get_user(1000)  # Get the user with the uid 1000
        get_user('methmal') # Get the user with the name methmal
        get_user(path='/etc/passwd') # Get the owner of /etc/passwd file
    '''
    ...


def get_group(group: int | str | None = None, path: str | None = None) -> struct_group:
    '''
    Get a unix group on different conditions

    Parameters:

        - group (optional): Gid(int) or groupname(str) of the group
        - path (optional): Relative file path(str) to find the group
    
    Returns:

        - (struct_group) a group

    Usage::

        get_group()  # Get the group primary group of the user who is running the program
        get_group(1000)  # Get the group with the gid 1000
        get_group('methmal') # Get the group with the name is methmal
        get_group(path='/etc/passwd') # Get the group of /etc/passwd file
    '''
    ...


def convert_permissions(mode: str) -> str:
    '''
    Convert file permissions from numeric mode to letters

    Parameters:

        - mode (str required): Numeric mode consist of 3 ocatal digits
    
    Returns:

        - (str) letter permissions
    
    Usage::

        perm = convert_permissions("550") 
        # perm = 'r-xr-x---'
    '''
    ...


FileType: TypeAlias = Literal[
    "f",
    "d",
    "c",
    "b",
    "p",
    "l",
    "s"
]

def find_file_type(path: str) -> FileType:
    '''
    Find the type of a given file
    
    Parameters:

        - path (str required): Relative path to the file

    Returns:

        - (FileType) type of the file as an single character
    
    Usage::

        find_file_type("/etc/sshd/sshd_config") # 'f'
        find_file_type("/dev/null") # 'c'
        find_file_type("/home") # 'd'
        find_file_type("/dev/sda") # 'b'
    '''
    ...