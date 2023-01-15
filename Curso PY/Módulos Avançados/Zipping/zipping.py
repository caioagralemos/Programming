import zipfile

f = open('file.txt', 'w')
f.write("my file!")
f.close()

f = open('file2.txt', 'w')
f.write("my second file!")
f.close()

comp_file = zipfile.ZipFile('zippedfile.zip', 'w')
comp_file.write('file.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

