import requests
version_url = "\\netstore-ch\R&D TN China\R&D_Server\Version Management\Dev_Version\Version to V&V\NPTI\V7.0\V7.0 Highlights.xlsx"

r = requests.get(version_url) # create HTTP response object

with open("python_logo.png",'wb') as f:
    f.write(r.content)