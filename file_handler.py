"""
Code used to read/write from files.
TODO: finish documentation
"""
import code_replacer as cr
import tokens
from shutil import copytree, rmtree
from os.path import isdir
from os import listdir

def delete_new_dir(src_path):
    rmtree(src_path)

def copy_to_new_dir(src_path, dest_path):
    copytree(src_path, dest_path)

def DFS(path, ext, template_path):
    """
    Performs depth first search on the directory given. Searches directory for
    all files that end with extention inputed.
    :param path: string representing a directory OR path to search through and
                alter code
    :param ext: string representing extention to search for
    """
    if isdir(path):
        for directory in listdir(path):
            DFS(path + "\\" + directory, ext, template_path)
    else:
        if path.endswith(ext):
            prep_code(path, template_path)

#TODO: fix template
def prep_code(code_path, template_path):
            code = read_code_from_file(code_path)
            template = read_code_from_file(template_path)
            title = code_path.split("\\")[-1]
            code = cr.search_and_alter_code(template, {'code': code, 'title': [title]})
            code = cr.search_and_alter_code(code, tokens.token_dic)
            write_code_to_file(code, code_path)


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