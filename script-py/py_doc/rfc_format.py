
with open('1.txt', 'r') as fpr:
    content = fpr.read()
content = content.replace('\n', '')

with open('test1.txt', 'w+') as fpw:
    fpw.write(content)