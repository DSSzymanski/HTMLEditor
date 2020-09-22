"""
Code used to read/write from files.
"""
import code_replacer as cr
import navbar
from shutil import copytree
from os.path import isdir
from os import listdir

def copy_to_new_dir(src_path, dest_path):
    copytree(src_path, dest_path)

def DFS(path, ext):
    """
    Performs depth first search on the directory given. Searches directory for
    all files that end with extention inputed.
    :param path: string representing a directory OR path to search through and
                alter code
    :param ext: string representing extention to search for
    """
    if isdir(path):
        for directory in listdir(path):
            DFS(path + "\\" + directory, ext)
    else:
        if path.endswith(ext):
            code = read_code_from_file(path)
            #TODO change to tokens from empty dictionary
            code = cr.search_and_alter_code(code, navbar.tokens)
            write_code_to_file(code, path)


def read_code_from_file(fileLocation):
    """
    Opens HTML file and returns code as a list of strings
    :param fileLocation: path to HTML file
    """
    code = []
    with open(fileLocation, "r") as f:
        for line in f:
            code.append(line)
    return code

def write_code_to_file(code, fileLocation):
    """
    Writes code given to file location.
    :param code: list of strings representing code.
    :param fileLocation: path to write to.
    """
    with open(fileLocation, 'w') as f:
        f.writelines(code)