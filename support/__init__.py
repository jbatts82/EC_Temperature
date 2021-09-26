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
    output = header + str(body)
    print(output)

def div():
	print("###############################################################################")
	
    
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))