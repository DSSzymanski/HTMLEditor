import navbar
"""
TODO: split into 2 main files. 1 for file handling / recreating file structure
and one for actually altering the code
"""
#TODO: move to file handler file
def getCodeFromFile(fileLocation):
    """
    Opens HTML file and returns code as a list of strings
    :param fileLocation: path to HTML file
    """
    code = []
    with open(fileLocation, "r") as f:
        for line in f:
            code.append(line)
    return code

#print(getCodeFromFile("C:\\Users\\Daniel\\Desktop\\Code_Orange.html"))