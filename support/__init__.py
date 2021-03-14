###############################################################################
# File Name  : __init__.py
# Date       : 03/14/2021
# Description: Support Functions Package
###############################################################################

def log(header, body):
    colon_spaces = 19
    while len(header) < colon_spaces:
        header = header + " "
    header = header + ": "
    output = header + body
    print(output)