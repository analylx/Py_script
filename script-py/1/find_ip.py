import re
#run on VS code need focus the dir, can change the pwd from below window.otherwise change the path to absolute path.
with open("e:/script-py/1/ifconfig.txt", 'r') as f:
    lines= f.readlines()
    for line in lines:
        result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", line)
        if result:
            print result
