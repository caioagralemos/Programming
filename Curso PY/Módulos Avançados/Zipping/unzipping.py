import zipfile

zip_obj = zipfile.ZipFile('zippedfile.zip', 'r')
zip_obj.extractall('extracted_cont')