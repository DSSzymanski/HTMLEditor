def getCodeFromFile(fileLocation):
    """
    Opens HTML file and returns code as an array of strings
    :param fileLocation: path to HTML file
    """
    codeList = []
    with open(fileLocation, "r") as f:
        for line in f:
            codeList.append(line)
    return codeList

#print(getCodeFromFile("C:\\Users\\Daniel\\Desktop\\Code_Orange.html"))