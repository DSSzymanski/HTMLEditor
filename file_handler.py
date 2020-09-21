"""
Code used to read/write from files.
"""
from os.path import isdir
from os import listdir

def DFS(path, ext):
    if isdir(path):
        for directory in listdir(path):
            DFS(path + "\\" + directory, ext)
    else:
        if path.endswith(ext):
            print(path)

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
    pass