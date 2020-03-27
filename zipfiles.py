import zipfile, os


exampleZip = zipfile.ZipFile('data/data_zipfilesPY.zip')
print(exampleZip.namelist())

# spamInfo = exampleZip.getinfo('spam.txt')

# print(spamInfo.file_size)
# print(spamInfo.compress_size)

# print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo .compress_size, 2)))

# exampleZip.close()