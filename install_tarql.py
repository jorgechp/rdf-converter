import os
import stat
import zipfile
import requests
import tempfile


url = "https://github.com/tarql/tarql/releases/download/v1.2/tarql-1.2.zip"

with tempfile.TemporaryDirectory() as temp_dir:
    print("Downloading from " + url)

    response = requests.get(url)
    file_path = temp_dir + '/' + "tarql.zip"
    f = open(file_path, "wb")
    f.write(response.content)
    f.close()

    print("File downloaded at " + file_path)
    with zipfile.ZipFile(file_path) as item:
        item.extractall()
    print("Extracted files")
    st = os.stat('tarql-1.2/bin/tarql')
    os.chmod('tarql-1.2/bin/tarql', st.st_mode | stat.S_IEXEC)
    print("Giving execution permissions to tarql executable")
    print("Done")
