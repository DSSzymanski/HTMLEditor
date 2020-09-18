"""
This module is designed to alter code given token variables. Searches through
inputed code looking for the tokens ("{***" and "***}") and replaces them with
different code given the string in between the two tokens.

The altering of code looks at the line of the token and copies the indentation
style of that line and adds it to the new code being added so it retains the same
indentation. Note: does not change the existing indentation within the new code,
just adds to the beginning.

Module is used by just calling the search_and_alter_code method. It takes in
code represented by a list of strings for lines and a dictionary of terms mapping
to code chunks to replace.

Example:
    search_and_alter_code(html_code, token_strings)
"""
def search_and_alter_code(code, tokens):
    """
    Main algorithm for altering code files. Searches code for token lines,
    replaces tokens with code, and returns code.
    :param code: list of strings representing code.
    :param tokens: dictionary relating tokens to arrays of strings representing
        lines of code.
    """
    token_ids = ["{***", "***}"]
    for pos, line in enumerate(code):
        #checks if the line contains both starting and ending token identifiers
        if all(id in line for id in token_ids):
            token, indentation = _extract_token(snippet=line, token_ids=token_ids)
            code = _replace(code=code, pos=pos, token=token, tokens=tokens,\
                           indentation=indentation)
    return code

def _replace(code, pos, token, tokens, indentation):
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
        replacement = _indent_code(code=replacement, indentation=indentation)
    #no code chunk found
    else:
        return code
    return code[:pos] + replacement + code[pos+1:]

def _indent_code(code, indentation):
    """
    Takes list of strings and indents them using the indentation of the stripped
    line from the _extract_token method.
    :param code: list of strings representing code.
    :param indentation: string of indentation. Retains tab/spacing from line used.
    """
    return [indentation + line for line in code]

def _extract_token(snippet, token_ids):
    """
    Extracts token from line of code and the amount of indentation.
    :param snippet: line of code
    :param token_ids: tokens to strip from line of code
    """
    #used for removing token identifier spacing
    token_id_len = len(token_ids[0])
    left = snippet.find(token_ids[0])
    right = snippet.find(token_ids[1])
    return snippet[left+token_id_len:right], snippet[:left]
