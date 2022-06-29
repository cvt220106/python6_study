# r-只读模式,对应file的read(),readline(), readlines()函数
file = open('a.txt', 'r', encoding='utf-8')
# print(file.read()) # 输出整个文件内容
# print(file.readline()) # 输出文件的第一行的内容
print(file.readlines())  # 将文件的一行行类容作为一个列表输出
file.close()
