def getCodeFromFile(fileLocation):
    """
    Opens HTML file and returns code as string
    :param fileLocation: path to HTML file
    """
    with open(fileLocation, "r") as f:
        return f.read()