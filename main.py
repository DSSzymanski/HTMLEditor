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
    codeList = []
    with open(fileLocation, "r") as f:
        for line in f:
            codeList.append(line)
    return codeList

#print(getCodeFromFile("C:\\Users\\Daniel\\Desktop\\Code_Orange.html"))

#TODO: move code below into code altering file
