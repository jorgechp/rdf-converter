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
    print("Done")
