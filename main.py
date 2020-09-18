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
    codeList = []
    with open(fileLocation, "r") as f:
        for line in f:
            codeList.append(line)
    return codeList

#print(getCodeFromFile("C:\\Users\\Daniel\\Desktop\\Code_Orange.html"))

#TODO: move code below into code altering file
def searchAndAlterCode(code, tokens):
    """
    Main algorithm for altering code files. Searches code for token lines,
    replaces tokens with code, and returns code.
    :param code: list of strings representing code.
    :param tokens: dictionary relating tokens to arrays of strings representing
        lines of code.
    """
    tokenIds = ["{***", "***}"]
    for pos, line in enumerate(code):
        #checks if the line contains both starting and ending token identifiers
        if all(id in line for id in tokenIds):
            token, indentation = extractToken(snippet=line, tokenIds=tokenIds)
            code = replace(code=code, pos=pos, token=token, tokens=tokens,\
                           indentation=indentation)
    return code

def replace(code, pos, token, tokens, indentation):
    """
    Search if token has an associated code chunk related to it.
    Removes token line and returns the code page with code chunk instead if found.
    Returns original code if not found.
    :param code: list of strings representing code.
    :param pos: position of token line in code list.
    :param tokens: dictionary relating tokens to arrays of strings representing
        lines of code.
    :param indentation: string of indentation to space code (retains tabs/spaces).
    """
    if token in tokens:
        #retrieve code from dictionary attributed to the token
        replacement = tokens[token]
        replacement = indentCode(code=replacement, indentation = indentation)
    #no code chunk found
    else:
        return code
    return(code[:pos] + replacement + code[pos+1:])

def indentCode(code, indentation):
    return [indentation + line for line in code]

def extractToken(snippet, tokenIds):
    """
    Extracts token from line of code and the amount of indentation.
    :param snippet: line of code
    :param tokenIds: tokens to strip from line of code
    """
    #used for removing token identifier spacing
    tokenIdLen = len(tokenIds[0])
    left = snippet.find(tokenIds[0])
    right = snippet.find(tokenIds[1])
    return snippet[left+tokenIdLen:right], snippet[:left]
"""
tokens = navbar.tokens
code = getCodeFromFile("C:\\Users\\Daniel\\Desktop\\Code_Orange.html")
print(searchAndAlterCode(code=code, tokens= tokens))
"""