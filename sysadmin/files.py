#!/usr/bin/python
import os
import shutil
import pwd
import grp
from sysadmin import utils

def echo(content, path = None, append = True):
    if path == None:
        print(content)
    else:
        operation = 'a' if append == True else 'w'
        with open(path, operation) as file:
            file.write(f"{content}\n")


def cat(path):
    if not os.path.exists(path):
        raise Exception(f"{path}: No such file or directory")

    content = ""
    with open(path, 'r') as file:
        for line in file:
            content += line
    return content


def touch(path):
    if not os.path.exists(path):
        basepath = os.path.dirname(os.path.realpath(path))
        if not os.path.exists(basepath) :
            raise Exception(f"touch: cannot touch '{path}': No such file or directory")
        else:
            with open(path, 'w') as file:
                pass


def rmdir(path):
    if not os.path.exists(path):
        raise Exception(f"rmdir: failed to remove '{path}': No such file or directory")
    
    if not os.path.isdir(path):
        raise Exception(f"rmdir: failed to remove '{path}': Not a directory")
 
    shutil.rmtree(path)


def rm(path, recursive=False):
    if not os.path.exists(path):
        raise Exception(f"rm: cannot remove '{path}': No such file or directory")
    
    if os.path.isdir(path):
        if recursive == False:
            raise Exception(f"rm: cannot remove '{path}': Is a directory")
        shutil.rmtree(path)
    else:
        os.remove(path)


def mkdir(path, parents=False):
    if parents == True:
        if not os.path.exists(path):
            return os.makedirs(path)

    if os.path.exists(path):
        raise Exception(f"mkdir: cannot create directory '{path}': File exists")
    
    basepath = os.path.dirname(os.path.realpath(path))
    if not os.path.exists(basepath) :
        raise Exception(f"mkdir: cannot create directory '{path}': No such file or directory")
    else:
        return os.mkdir(path)


def grep(path, pattern):
    pass


def head(path, line_count=10):
    if not os.path.exists(path):
        raise Exception(f"head: cannot open '{path}' for reading: No such file or directory")

    lines = []
    with open(path, 'r') as file:
        for i, line in enumerate(file):
            if i == line_count:
                return lines
            else:
                lines.append(line.rstrip("\n"))


def tail(path, line_count=10):
    with open(path, 'rb') as file:
        file.seek(0, 2)  # Move to the end of the file
        file_size = file.tell()
        lines = [] 
        line_count = 0 
        position = file_size - 1

        while line_count < line_count and position >= 0:
            file.seek(position)  # Move to current position
            current_char = file.read(1) 
            if current_char == b'\n':
                # Found a newline character, so read the line
                line = file.readline().decode().strip()
                lines.append(line) 
                line_count += 1 
            position -= 1

        lines.reverse()
        return lines
    

def wc(path):
    pass

def du(path):
    pass

def ln(source: str, target: str, symbolic:bool = False) -> None:
    pass

# TODO - list number of links to a file
def ls(path: str | None = None):
    if path == None:
        path = os.getcwd()

    if os.path.isdir(path):
        files = os.listdir(path)
    else:
        files = [path]

    output = []
    for file in files:
        stat = os.stat(path, follow_symlinks=False)
        uid = stat.st_uid
        gid = stat.st_gid
        mode = str(oct(stat.st_mode)[-3:])

        output.append({
            "name": file,
            "inode": stat.st_ino,
            "mode": mode,
            "permissions": utils.convert_permissions(mode),
            "owner": pwd.getpwuid(uid).pw_name,
            "group": grp.getgrgid(gid).gr_name,
            "link_count": stat.st_nlink,
            "size": stat.st_blksize,
            "mtime": stat.st_mtime,
            "ctime": stat.st_ctime,
        })

    return output

files = ls()
for file in files:
    print(f"{file["name"]} {file["link_count"]}")